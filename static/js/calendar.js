let calendarEl = document.querySelector("#calendar");


var calendar = "";

document.addEventListener('DOMContentLoaded', function() {
    fetch('/get-dates')
    .then(res => res.json())
    .then(data => {
        console.log(data.events);
        console.log(data.x);
        let calendar = new FullCalendar.Calendar(calendarEl, {
             events: data.events
        });
        calendar.render();
    });
});


// document.addEventListener('DOMContentLoaded', function() {
//     calendar = new FullCalendar.Calendar(calendarEl, {
//          events: '/get-dates',
//          selectable: true,
//          select: function(start, end, allDays) {
//             console.log(start);
//          }
//     });
//     calendar.render();
// });


















// eventClick: function(info) {
//     alert('Event: ' + info.event.title);
//     alert('Coordinates: ' + info.jsEvent.pageX + ',' + info.jsEvent.pageY);
//     alert('View: ' + info.view.type);

//     // change the border color just for fun
//     info.el.style.borderColor = 'red';
//   }