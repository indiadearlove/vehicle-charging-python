# Vehicle Charging

```
pip install -r requirements.txt
python manage.py runserver

npm install bootstrap reactstrap axios --save
npm start
```

- Go to http://localhost:8000/admin/auth/user/ and add a user
- Add a company http://localhost:8000/admin/company/company/
- Add vehicles through the django admin
  Note: I've hard coded in the vehcile id 2 so you will need to create 2 vehicles
- Add charges through the django admin
  Note: If there are no charges for a vehicle then the car is not plugged in so the dashboard will be empty
- Go to http://localhost:3000/
  

### Technologies used

- Python
- Django Framework
- SQLite DB (postgres would probably be more appropriate in the long run)
- React

### Assumptions made

- Individual companies would want thier own styling
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

- Thought about scalibility
- In the backend I followed Python and Django coding standards
- I added certain fields to models they weren't needed at this stage but it would be good for us to have that data in the future
- The little frontend I did was with mobile first in mind as assume that is what the user would want
