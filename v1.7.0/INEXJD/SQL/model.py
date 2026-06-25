from ..functions.getJsonContent import getJsonContent
from ..functions.writeJsonContent import writeJsonContent
from .schema_validation import validate_record, get_table_schema


class Model:
    """
    Base ORM class for INEXJD models.
    Subclass this to create table-specific models!
    """
    _table_name = None
    
    def __init__(self, **kwargs):
        self._data = kwargs
    
    def __getattr__(self, name):
        return self._data.get(name)
    
    def __setattr__(self, name, value):
        if name.startswith("_"):
            super().__setattr__(name, value)
        else:
            self._data[name] = value
    
    def to_dict(self):
        return self._data.copy()
    
    @classmethod
    def create(cls, **kwargs):
        """Create and save a new record."""
        if not cls._table_name:
            raise ValueError("Model must define _table_name")
        
        schema = get_table_schema(cls._table_name)
        if schema:
            valid, errors, processed = validate_record(kwargs, schema, cls._table_name)
            if not valid:
                raise ValueError(f"Validation failed: {', '.join(errors)}")
            record_data = processed
        else:
            record_data = kwargs
        
        data = getJsonContent(cls._table_name)
        data.append(record_data)
        writeJsonContent(data, cls._table_name)
        return cls(**record_data)
    
    @classmethod
    def all(cls):
        """Get all records."""
        if not cls._table_name:
            raise ValueError("Model must define _table_name")
        data = getJsonContent(cls._table_name)
        return [cls(**row) for row in data]
    
    @classmethod
    def get(cls, **kwargs):
        """Get first matching record."""
        all_records = cls.all()
        for rec in all_records:
            match = True
            for k, v in kwargs.items():
                if rec._data.get(k) != v:
                    match = False
                    break
            if match:
                return rec
        return None
    
    def save(self):
        """Save current state to database."""
        if not self._table_name:
            raise ValueError("Model must define _table_name")
        
        data = getJsonContent(self._table_name)
        
        # Try to find existing record and update
        found = False
        for i, row in enumerate(data):
            # Find by id if exists
            if "id" in row and "id" in self._data and row["id"] == self._data["id"]:
                data[i] = self._data
                found = True
                break
        if not found:
            data.append(self._data)
        
        writeJsonContent(data, self._table_name)
