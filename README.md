# Base API Framework

A reusable framework for creating dynamic, model-based API endpoints in Django using Django REST Framework (DRF).

## Features

- **Dynamic Model Assignment**: Use the same API logic for multiple models.
- **Automatic Serialization**: Automatically generate serializers with all fields included.
- **Query Filtering**: Supports filtering querysets based on URL query parameters.

## Installation

1. Clone the repository.
2. Ensure you have Django and Django REST Framework installed.
3. Integrate the provided classes into your Django project.

## Components

### 1. `BaseSerializer`

A dynamic serializer that automatically binds to the specified model.