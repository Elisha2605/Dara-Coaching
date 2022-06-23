
var calendar = "";
document.addEventListener('DOMContentLoaded', function() {
    let calendarElement = document.querySelector("#calendar");
    calendar = new FullCalendar.Calendar(calendarElement, {
         events: '/get-dates'
    });
    calendar.render();
});