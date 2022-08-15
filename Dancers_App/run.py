"""Instead of running the application directly from the controller , we
create a separate file In order to remove unnecessary code from the controller
that does not pertain to the actual business logic. """

from views import app

app.run(debug=True)