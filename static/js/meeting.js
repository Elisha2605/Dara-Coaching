const meetingsElement = document.querySelector("#meetings")
const exercises = document.querySelector("#exercises")

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


fetch("/api-fetch-exercises")   
.then(res => res.json())
.then(data => {
    data.exercises.forEach(exercise => {
        
    })
})



async function create_exercise() {
    const clicked_exercise = event.target
    let exercise = clicked_exercise.innerHTML
    console.log(exercise)

    const connection = await fetch(`/api-create-meeting-exerises/${81}`, {
        method: "POST",
        body: exercise
    })
    if (!connection.ok) {
        alert("Could not connect")
        return
    }
}

