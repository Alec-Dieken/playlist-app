### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?

```
Postgres is an RDBMS that uses and extends SQL to access/manipulate databases.
```

- What is the difference between SQL and PostgreSQL?

```
SQL is a language used for accessing database information. PostgreSQL is a database system that uses and extends SQL for manipulating it's data.
```

- In `psql`, how do you connect to a database?

```
\c <database>
```

- What is the difference between `HAVING` and `WHERE`?

```
HAVING can be used with aggregates whereas WHERE cannot
```

- What is the difference between an `INNER` and `OUTER` join?
```
Inner join only includes the information from joined tables that is related. Outer join will return all data, related or not.
```

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
```
Left join will keep the unrelated information from just the first table. Right join will keep the unrelated information from the second table.
```

- What is an ORM? What do they do?
```
ORM stands for Object-Relational Mapping which lets you query and interact with databases through OOP. i.e. flask-sqlalchemy
```

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
```
With ajax you can make requests and update information without reloading the page.
```

- What is CSRF? What is the purpose of the CSRF token?
```
CSRF stands for cross site request forgery which is where attackers execute malicious requests from a user that the web application already trusts.
```

- What is the purpose of `form.hidden_tag()`?
```
It generates a hidden field that holds a unique token to prevent CSRF attacks.
```
