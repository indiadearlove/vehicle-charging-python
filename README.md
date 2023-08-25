# Vehicle Charging

```
pip install -r requirements.txt
python manage.py migrate
python manage.py run_factories
python manage.py runserver

npm install bootstrap reactstrap axios --save
npm start
```

- Go to http://localhost:3000/ to view app

- View django admin http://localhost:8000/

### Technologies used

- Python
- Django Framework
- SQLite DB (postgres would probably be more appropriate in the long run)
- React

### Assumptions made

- Individual companies would want their own styling
- Users would use mobile or a small device
- Battery charging is linear


### Spend time on

- architecture thinking of what data we would want to capture and what the user needs to see
- backend working on creating the APIs

### Less time on

- spent time setting up the frontend but little time styling, the little styling I did was inline which usually I would never do
- frontend files are pretty much all auto generated, would like to spend time sorting and creating individual components rather than all in one disorganised file
- Connecting up the schedule to auto create charges
- No time on tests!

### how you designed the system bearing in mind its end use

- Thought about scalability
- In the backend I followed Python and Django coding standards
- I added certain fields to models they weren't needed at this stage but it would be good for us to have that data in the future
- The little frontend I did was with mobile first in mind as assume that is what the user would want
