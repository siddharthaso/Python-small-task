"""script"""

In [5]: Blog.objects.create(name="testing blog 1")
Out[5]: <Blog: testing blog 1>

In [6]: Blog.objects.create(name="testing blog 2")
Out[6]: <Blog: testing blog 2>

In [7]: Blog.objects.create(name="testing blog 3")
Out[7]: <Blog: testing blog 3>

In [17]: b=Blog.objects.all()[0]

In [18]: e = Entry.objects.create(headline="This is beaking news", pub_date="2022-12-01",mod_date="2022-12-01", number_of_comments=2
    ...: , number_of_pingbacks= 2 , rating=5, blog=b)

In [19]: e.save()

In [29]: e = Entry.objects.create(headline="not an option", pub_date="2021-12-05",mod_date="2021-12-01", number_of_comments=2, numbe
    ...: r_of_pingbacks= 2 , rating=5, blog=b)

In [30]: e.author = a

In [31]: e.author
Out[31]: <Author: siddharth>

In [46]: e.authors.set((a,a1))

In [47]: e.authors
Out[47]: <django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager at 0x201a5478408>

In [48]: e.authors.all()
Out[48]: <QuerySet [<Author: siddharth>, <Author: keval>]>

In [49]: e.save()

In [50]: e = Entry.objects.create(headline="news", pub_date="2021-12-05",mod_date="2021-12-01", number_of_comments=2, number_of_ping
    ...: backs= 2 , rating=5, blog=b1)

In [51]: e.save()

In [52]: e = Entry.objects.create(headline="siddharth", pub_date="2022-12-05",mod_date="2022-12-01", number_of_comments=2, number_of
    ...: _pingbacks= 2 , rating=5, blog=b2)

In [53]: e.save()

In [54]: Blog.objects.create(name="blog 3 or 4")
Out[54]: <Blog: blog 3 or 4>

In [56]: b3=Blog.objects.all()[3]

In [57]: e = Entry.objects.create(headline="earth", pub_date="2002-12-05",mod_date="2002-12-01", number_of_comments=2, number_of_pin
    ...: gbacks= 2 , rating=5, blog=b3)

In [58]: e.save()

In [59]: Blog.objects.filter(entry__headline__contains='news', entry__pub_date__year=2022)
Out[59]: <QuerySet [<Blog: Beatles Blog>]>

In [60]: Blog.objects.all()
Out[60]: <QuerySet [<Blog: Beatles Blog>, <Blog: testing blog 1>, <Blog: testing blog 2>, <Blog: testing blog 3>, <Blog: blog 3 or 4>]>

In [61]: Blog.objects.filter(entry__headline__contains='siddharth', entry__pub_date__year=2022)
Out[61]: <QuerySet [<Blog: testing blog 2>]>

In [62]: Blog.objects.filter(entry__headline__contains='siddharth').filter(entry__pub_date__year=2022)
Out[62]: <QuerySet [<Blog: testing blog 2>]>

In [63]: Blog.objects.filter(entry__headline__contains='siddharth')
Out[63]: <QuerySet [<Blog: testing blog 2>]>

In [64]: Blog.objects.filter(entry__headline__contains='news')
Out[64]: <QuerySet [<Blog: Beatles Blog>, <Blog: testing blog 1>]>

In [65]: Entry.objects.all()
Out[65]: <QuerySet [<Entry: This is beaking news>, <Entry: not an option>, <Entry: news>, <Entry: siddharth>, <Entry: earth>]>

In [66]: Blog.objects.filter(entry__headline__contains='siddharth')
Out[66]: <QuerySet [<Blog: testing blog 2>]>

In [67]: Blog.objects.filter(entry__headline__contains='arth')
Out[67]: <QuerySet [<Blog: testing blog 2>, <Blog: testing blog 3>]>

In [68]: Blog.objects.filter(entry__headline__contains='arth').filter(entry__pub_date__year=2022)
Out[68]: <QuerySet [<Blog: testing blog 2>]>

In [69]: Blog.objects.filter(entry__headline__contains='arth').filter(entry__pub_date__year=2002)
Out[69]: <QuerySet [<Blog: testing blog 3>]>

In [70]: Entry.objects.all()[0:1]
Out[70]: <QuerySet [<Entry: This is beaking news>]>

In [71]: Entry.objects.all()[0:1].get()
Out[71]: <Entry: This is beaking news>

In [72]: Blog.objects.filter(entry__pub_date__year=2022)
Out[72]: <QuerySet [<Blog: Beatles Blog>, <Blog: testing blog 2>]>

In [73]: Blog.objects.filter(entry__pub_date__year=2002)
Out[73]: <QuerySet [<Blog: testing blog 3>]>

In [74]: Blog.objects.filter(entry__headline__contains='arth').filter(entry__pub_date__year=2022)
Out[74]: <QuerySet [<Blog: testing blog 2>]>

In [75]: print(Blog.objects.filter(entry__headline__contains='arth').filter(entry__pub_date__year=2022).sql)
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-75-0155f1283744> in <module>
----> 1 print(Blog.objects.filter(entry__headline__contains='arth').filter(entry__pub_date__year=2022).sql)

AttributeError: 'QuerySet' object has no attribute 'sql'

In [76]: print(Blog.objects.filter(entry__headline__contains='arth').filter(entry__pub_date__year=2022).query)
SELECT "model_orm_blog"."id", "model_orm_blog"."name", "model_orm_blog"."tagline" FROM "model_orm_blog" INNER JOIN "model_orm_entry" ON ("model_orm_blog"."id" = "model_orm_entry"."blog_id") INNER JOIN "model_orm_entry" T3 ON ("model_orm_blog"."id" = T3."blog_id") WHERE ("model_orm_entry"."headline" LIKE %arth% ESCAPE '\' AND T3."pub_date" BETWEEN 2022-01-01 AND 2022-12-31)

In [77]: print(Blog.objects.filter(entry__headline__contains='arth', entry__pub_date__year=2022).query)
SELECT "model_orm_blog"."id", "model_orm_blog"."name", "model_orm_blog"."tagline" FROM "model_orm_blog" INNER JOIN "model_orm_entry" ON ("model_orm_blog"."id" = "model_orm_entry"."blog_id") WHERE ("model_orm_entry"."headline" LIKE %arth% ESCAPE '\' AND "model_orm_entry"."pub_date" BETWEEN 2022-01-01 AND 2022-12-31)


from datetime import date
beatles = Blog.objects.create(name='Beatles Blog')
pop = Blog.objects.create(name='Pop Music Blog')
Entry.objects.create(
    blog=beatles,
    headline='New Lennon Biography',
    pub_date=date(2008, 6, 1),
)
Entry.objects.create(
    blog=beatles,
    headline='New Lennon Biography in Paperback',
    pub_date=date(2009, 6, 1),
)
Entry.objects.create(
    blog=pop,
    headline='Best Albums of 2008',
    pub_date=date(2008, 12, 15),
)
Entry.objects.create(
    blog=pop,
    headline='Lennon Would Have Loved Hip Hop',
    pub_date=date(2020, 4, 1),
)
Blog.objects.filter(
    entry__headline__contains='Lennon',
    entry__pub_date__year=2008,
)
Blog.objects.filter(
    entry__headline__contains='Lennon',
).filter(
    entry__pub_date__year=2008,
)