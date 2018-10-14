# pHarmr

## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```
### What is the name of your project?
```
pHarmr
```

### Describe your project!
pHarmr is a Hydroponics set up coupled with extensive monitoring and adjusting software.  With the help of pHarmr, users can monitor the health of their plants from miles away.  In dangerous climates minimal interaction with the crops is paramount, pHarmr allows users to adjust their crops' environment without needing to interact (and possibly contaminate) the plants.  Additionally, pHarmr can teach people with little to no experience in growing their own food how to provide their plants with the healthiest environment.  In the future, harvesters could simply share scripts--including the basic environmental needs of a plant--to teach other users how to grow a particular plant.

### Who made this amazing Hack?
James C., Rishab Nayak, Jason Smith, Emily Vogelsperger

### What inspired you to make this?
James:

Rishab:

Jason:

Emily: I was inspired to join this project because I personally have no experience in hydroponics and I was interested in joining a very diverse group.  Each person in this group brought specific talents that were unique to the rest of the group.  It was incredibly rewarding to take an idea (of which I knew none of the background) and hear so many different points of view on how to tackle this problem.  Also, I got exposure to some interesting hardware, which I know nothing about.

### What does your project do?
pHarmr uses multiple sensors--pH, temperature, moisture--and feeds the real-time values through a Raspberry Pi
and to a server.  Our web application then polls the server for these values and displays them neatly on the screen.  
If the user adjusts any of the sensors, the whole process is reversed until the sensor receives the adjust instruction.

### How did you build it?
Hardware:

Software: The front-end web application uses a Vue framework with JavaScripting.  For the server we used Adafruit,
which connects directly to the Raspberry Pi.

### What challenges did you face?
None of us had made a server before!  We all spent a considerable amount of time learning Google IoT, Could Firestore,
and Adafruit in order to get this project up and running.  While learning this very complicated and extremely new skill
was daunting and frustrating at times, we are all ecstatic that we were able to accomplish something big we had never
done before.

Additionally, we all ran into lots of trouble while figuring out how to poll our server, send HTTP requests, and feed
these values into our Vue web application.  Again--these were all things we hadn't done before!  All-in-all, it was
an incredibly rewarding experience.

Finally, we had a lot of trouble actually displaying the values we got from out polled data.  Unfortunately it was very difficult to simply display our real-time data in our HTML tag.

### What accomplishments are you proud of?
Definitely receiving that first 200 response from our HTTP request (and it actually contained the correct values)!  
Another big accomplishment was setting up our Raspberry-Pi with the Adafruit server.  This is mainly because we spent
almost all of the beginning stages of the hackathon trying to learn Google Cloud IoT and Cloud Firestore and we were
glad to see some progress.
Finally figuring out how to poll the server on JavaScript--WITHOUT destroying our memory--was probably our greatest accomplishment of the night.  This was a problem we spent many hours on and asked many mentors for help with.  

### What did you learn while building this?
A lot of the software we were working with are extremely finicky.  It was very difficult to debug--especially since this
was all of our first times actually implementing this!  We all learned the importance of starting small first.  We
continually created small goals for the team which kept us from thinking too big, too fast, and in turn motivated us
because we were actually accomplishing things!

### What's next for your project?
We hope to fully flesh this project out so that it can be available for people in harsh climates, impoverished areas,
and those who simply enjoy growing their own food!

Instead of polling the server, we would love to find a way to rework the backend so that we can push the real-time data
to our web application.  Without monetary limitations, we could improve our hardware so that more sensors could be
added without overloading the Raspberry Pi.  In future implementations, pHarmr would allow users to create and share
their environment scripts with others, sharing their first-hand knowledge growing that particular plant.

### What did you build it with?
Front-End framework is Vue.js, while the server is run on Adafruit.  Our sensors connect to our Raspberry-Pi which in
turn sends the sensor information to Adafruit.  Using XMLHttpRequests, we are able to poll from the server to retrieve
the sensor data.
