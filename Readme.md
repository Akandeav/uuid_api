# UUID API
A simple API to return key-value pair of randomly generated UUID. 
Key will be the timestamp while value is the UUID. The API returns all previous UUID ever generated by the API.  
**Example**
>{

"2021-05-21 12:10:19.484523": "e8c928fea580474cae5aa3934c59c26f"

"2021-05-21 12:08:25.751933": "fcd25b46bec84ef79e14410b91fbf0b3",

"2021-05-21 12:07:27.150522": "6270d1d412b546a28b7d2c98130e1a5a",

}

## Requirements
- Anaconda or Miniconda

## installation
1. Create virtual environment from ```environment.yml``` file:  
```conda env create -f environment.yml```
2. Activate the enivironment ```mcro```  
```conda activate mcro```
3. Verify the environment was installed correctly:  
```conda env list```

## Usage
1. Ensure virtual environment is installed.
2. Start Django server.  
```python manage.py runserver```
3. Access api route ```http://localhost:8000/api/uuid``` or ```127.0.0.1``` in place of localhost.

## Support
- If you are familar with django you can set up your environment on your own without conda.
- Docker version of api available [here](https://gi)
- Need help contact [ME](mailto:akandevic@gmail.com?subject=Support:UUID-API)