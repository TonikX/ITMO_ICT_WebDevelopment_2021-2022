# Welcome to Hotel App

## Description
Hotel provides a simulated hotel system that can manage visitors, hosts, hotels, rooms, bookings and bills

## Model Explanation

- `User` is a base user of hotel app, which can be `Visitor` or `Host`, in which they can sign up and log in with different role & permission
- `Visitor` can view `Hotel`, available `Room` of the hotel and book.
- Once booked, a `Booking` is create to track the booking of visitor with the room in specific timeframe (date check in, date check out)
- `Bill` is all the cost associate with the `Booking`, which can be any services such as **stay**, **meal**, **extra people**...
