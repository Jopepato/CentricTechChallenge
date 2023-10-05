# Task 4 - SQL and Django ORM queries
Based on the following schema of tables/objects:
![schema](docs/schema.png)

We have to create a SQL query, that addresses the following statements:
Write a query (either in django ORM or in SQL) to extract, for every existing
product, the following fields:
- Product.Title
- Image.Url for the images with the ImageIndex = 0.
ImageIndex field states the priority order of images of a certain product.
So for a given ProductId, the image with ImageIndex = 0 would be the
most relevant image for that product
- ProductDescription.TranslatedText if exists, else
ProductDescription.OriginalText for ProductDescriptions in CountryCode =
‘us’


**SQL Query**

Here is the SQL query for the statements that we have mentioned before, we could do it with 
SQL subqueries as it's shown below or with `WITH` statements. Shown in the second version, depends on the team practices. 
The former version it's cleaner, we could also create views with the statements created for the secondary tables.
```SQL
SELECT 
  Product.Title, 
  Image.Url, 
  ProductDescription.Text 
FROM 
  Product 
  LEFT JOIN (
    SELECT 
      ProductImages.ProductId, 
      ProductImages.ImageId, 
      Image.Url 
    FROM 
      ProductImages 
    WHERE 
      ProductImages.ImageIndex = 0 
      INNER JOIN Image on ProductImages.ImageId = Image.Id
  ) AS Image ON Image.ProductId = Product.Id 
  LEFT JOIN (
    SELECT 
      ProductDescription.ProductId, 
      CASE WHEN ProductDescription.TranslatedText <> NULL THEN ProductDescription.TranslatedText
           WHEN ProductDescription.TranslatedText = NULL 
                AND ProductDescription.CountryCode = 'us' THEN ProductDescription.OriginalText 
           ELSE NULL END AS Text
  ) AS ProductDescription ON ProductDescription.ProductId = Product.Id
```

Version with `WITH` statements.
```SQL
WITH (
  SELECT 
    ProductImages.ProductId, 
    ProductImages.ImageId, 
    Image.Url 
  FROM 
    ProductImages 
  WHERE 
    ProductImages.ImageIndex = 0 
    INNER JOIN Image on ProductImages.ImageId = Image.Id
) AS Image WITH (
  SELECT 
    ProductDescription.ProductId, 
    CASE WHEN ProductDescription.TranslatedText <> NULL THEN ProductDescription.TranslatedText
         WHEN ProductDescription.TranslatedText = NULL 
              AND ProductDescription.CountryCode = 'us' THEN ProductDescription.OriginalText
         ELSE NULL END AS Text
) AS ProductDescription 
SELECT 
  Product.Title, 
  Image.Url, 
  ProductDescription.Text 
FROM 
  Product 
  LEFT JOIN Image ON Image.ProductId = Product.Id 
  LEFT JOIN ProductDescription ON ProductDescription.ProductId = Product.Id
```

**Django ORM**

Even though I haven't used Django ORM I'm going to give it a try for the sake of learning and to follow
the team's stack and technology. I've been checking ORM [documentation](https://docs.djangoproject.com/en/4.2/topics/db/queries/) to write the following query,
supposedly it will be creating the SQL query on the back, which will make this simpler.

```Python
from django.db.models import Case, When, Value

Product.objects.annotate(text = Case(
            When(ProductDescription.TranslatedText != null, then = Value(ProductDescription.TranslatedText)),
            When(ProductDescription.TranslatedText == null and ProductDescription.CountryCode == 'us', then = Value(ProductDescription.OriginalText)),
            default=Value('')
)).filter(productimages__imageindex = 0).values_list("Title", "Url", "text")
```

This was my best attempt at the Django ORM which can be probably improved or it may need some fixing when running it. However,
it was a good exercise of looking at the documentation and checking what could be done with this ORM, looking at real examples from
your codebase will also be a great learning experience :)