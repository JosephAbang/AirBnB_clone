# Models README

## BaseModel
### description

The `BaseModel` class serves as the foundation for other classes in this project, defining common attributes and methods that are shared among various objects.

### Attributes

- `id` (string): A unique identifier assigned to each instance using `uuid.uuid4()`. It ensures the uniqueness of each `BaseModel` object.

- `created_at` (datetime): The timestamp of when an instance is created, assigned with the current datetime.

- `updated_at` (datetime): The timestamp of when an instance is created and updated every time an object is modified.

### Methods

- `save(self)`: This method updates the `updated_at` attribute with the current datetime. Call this method whenever you want to save changes to your object.

- `to_dict(self)`: Returns a dictionary containing all the key-value pairs of the instance's attributes using `self.__dict__`. The following details apply:

  - Only instance attributes set will be returned.

  - A key `__class__` is added to the dictionary, containing the class name of the object.

  - The `created_at` and `updated_at` attributes are converted to string objects in ISO format (`%Y-%m-%dT%H:%M:%S.%f`, e.g., `2017-06-14T22:31:03.285259`). The `strftime(format)` method of the datetime object was used to achieve this.
