const meetingsElement = document.querySelector("#meetings")

fetch("/api-fetch-meetings")
.then(res => res.json())
.then(data => {
    data.meetings.forEach(meeting => {
        console.log(meeting);
        const newOp = document.createElement("pre");
        newOp.append(meeting.notes)
        meetingsElement.insertAdjacentElement("afterbegin", newOp)
    });
})