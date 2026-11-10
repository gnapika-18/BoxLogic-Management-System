Test Cases – BoxLogic


1. Products App

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| P01 | Create a product | Product should be created successfully |
| P02 | Verify product name | Product name should match |
| P03 | Verify product dimensions | Length, width and height should match |
| P04 | Verify product weight | Product weight should match |
| P05 | Verify product string representation | Product name should be returned |

2. Orders App

| Test ID | Test Scenario | Expected Result |
|---|---|---|
| O01 | Create an order | Order should be created successfully |
| O02 | Add product to order | Product should be associated with the order |
| O03 | Recommend a suitable box | A suitable box should be returned |
| O04 | No suitable box available | System should return None |
| O05 | Select cheapest suitable box | Cheapest suitable box should be selected |

3. Testing Framework

- Framework: Django TestCase
- Language: Python
- Database: Django test database
