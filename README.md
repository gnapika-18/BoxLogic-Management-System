# BoxLogic – AI-Assisted Box Selection System

## 1. Project Overview

PackWise is a Django-based web application designed to recommend suitable shipping boxes for ecommerce customer orders.

The system considers product dimensions, product weight, box dimensions, maximum weight capacity, and box cost to identify a suitable and cost-effective shipping box.

The main goal of this project is to simplify the packaging selection process and help warehouse teams choose appropriate shipping boxes for customer orders.

## 2. Project Objectives

- Manage ecommerce products and their dimensions.
- Manage customer orders and ordered products.
- Maintain shipping box details.
- Calculate the combined weight and approximate dimensions of an order.
- Recommend a suitable shipping box.
- Select the lowest-cost box among the suitable options.
- Display the recommendation along with box specifications and cost.

## 3. Technologies Used

 Technology - Purpose 
 Python - Backend programming 
 Django - Web application framework 
 HTML5 - Page structure 
 CSS3 - Styling and design 
 SQLite - Database 
 Django Admin - Managing products, orders and boxes 
 Django TestCase - Application testing 
 Git and GitHub - Version control and project hosting 

## 4. Application Features

### Products Management
- Add and manage products.
- Store product name.
- Store length, width and height.
- Store product weight.

### Orders Management
- Create customer orders.
- Associate products with orders.
- Maintain product quantities.
- View order details.

### Box Management
- Store box names.
- Maintain internal box dimensions.
- Store maximum weight capacity.
- Store box cost.

### Box Recommendation
- Calculate the total product weight.
- Calculate approximate combined order dimensions.
- Identify boxes that satisfy the dimension and weight requirements.
- Select the cheapest suitable box.
- Display a message when no suitable box is available.

## 5. Box Recommendation Logic

The application uses the following approach:

1. Retrieve the selected customer order.
2. Retrieve all products associated with the order.
3. Calculate total weight using product weight multiplied by quantity.
4. Calculate approximate order length by adding product lengths multiplied by quantities.
5. Use the maximum product width and height as the approximate order width and height.
6. Compare the calculated requirements with available box dimensions and weight capacity.
7. Select the suitable box with the lowest cost.

### Box Selection Conditions

A box is considered suitable when:

- Box length is greater than or equal to the calculated order length.
- Box width is greater than or equal to the maximum product width.
- Box height is greater than or equal to the maximum product height.
- Box maximum weight capacity is greater than or equal to the total order weight.

If multiple boxes satisfy these conditions, the application selects the cheapest one.

Note: This is a simplified dimension-based selection approach. It does not perform actual 3D packing, product rotation, or arrangement calculations. Therefore, it is an approximation rather than a guarantee of physical packing fit.

## 6. Installation and Setup

### Prerequisites

- Python 3.x
- pip
- Git

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd PackWise
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Step 5: Install Django

```bash
pip install django
```

If a `requirements.txt` file is available, install the dependencies using:

```bash
pip install -r requirements.txt
```

### Step 6: Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 7: Create a Superuser

```bash
python manage.py createsuperuser
```

### Step 8: Start the Development Server

```bash
python manage.py runserver
```

Open the application in your browser:

http://127.0.0.1:8000/

Django Admin:

http://127.0.0.1:8000/admin/

## 7. Testing

The application uses Django's built-in testing framework.

### Run Products App Tests

```bash
python manage.py test products
```

### Run Orders App Tests

```bash
python manage.py test orders
```

### Run All Tests

```bash
python manage.py test
```

Test cases cover product creation, order creation, product association, suitable box selection, unavailable boxes, and cheapest box selection.

Actual test execution results are documented in `TEST_OUTPUT.md`.

Test scenarios are documented in `TEST_CASES.md`.

## 8. Documentation

| File | Description |
|---|---|
| README.md | Project overview and setup instructions |
| TEST_CASES.md | Test scenarios and expected results |
| TEST_OUTPUT.md | Actual test execution output |
| AI_USAGE.md | Documentation of AI tools and assistance used |


## 9. Conclusion

BoxLogic demonstrates how a Django-based application can manage products and customer orders while recommending suitable shipping boxes based on product dimensions, weight capacity, and box cost.

The project provides a foundation for developing more advanced packaging optimization solutions.

## 10. Author

Project: BoxLogic – AI-Assisted Box Selection System

Repository: 
