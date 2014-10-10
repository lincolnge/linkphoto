$(document).ready(function() {
    /* initialize the external events
    -----------------------------------------------------------------*/

    $('#external-events .fc-event').each(function() {

        // create an Event Object (http://arshaw.com/fullcalendar/docs/event_data/Event_Object/)
        // it doesn't need to have a start or end
        var eventObject = {
            title: $.trim($(this).text()) // use the element's text as the event title
        };

        // store the Event Object in the DOM element so we can get to it later
        $(this).data('eventObject', eventObject);

        // make the event draggable using jQuery UI
        $(this).draggable({
            zIndex: 999,
            revert: true, // will cause the event to go back to its
            revertDuration: 0 //  original position after the drag
        });

    });


    /* initialize the calendar
    -----------------------------------------------------------------*/

    $('#calendar').fullCalendar({
        header: {
            left: 'prev,next today',
            center: 'title',
            right: 'month,agendaWeek,agendaDay'
        },
        // defaultDate: '2014-09-12',
        // selectable: true,
        // selectHelper: true,
        // select: function(start, end) {
        //     var title = prompt('Event Title:');
        //     var eventData;
        //     if (title) {
        //         eventData = {
        //             title: title,
        //             start: start,
        //             end: end
        //         };
        //         $('#calendar').fullCalendar('renderEvent', eventData, true); // stick? = true
        //     }
        //     $('#calendar').fullCalendar('unselect');
        // },
        // editable: true,
        eventLimit: true, // allow "more" link when too many events // 当有很多 events 时, 允许 "more" 链接
        events: {
            url: 'events_json',
            error: function() {

            }
        },
        editable: true, //允许拖动 
        droppable: true, // this allows things to be dropped onto the calendar !!!
        drop: function(date) { // this function is called when something is dropped

            // retrieve the dropped element's stored Event Object
            var originalEventObject = $(this).data('eventObject');

            // we need to copy it, so that multiple events don't have a reference to the same object
            var copiedEventObject = $.extend({}, originalEventObject);

            // assign it the date that was reported
            copiedEventObject.start = date._d;

            // render the event on the calendar
            // the last `true` argument determines if the event "sticks" (http://arshaw.com/fullcalendar/docs/event_rendering/renderEvent/)
            $('#calendar').fullCalendar('renderEvent', copiedEventObject, true);

            // is the "remove after drop" checkbox checked?
            if ($('#drop-remove').is(':checked')) {
                // if so, remove the element from the "Draggable Events" list
                $(this).remove();
            }

            // console.log(date)
            // console.log(originalEventObject)
            var d = new Date();
            console.log(d.toJSON())
            console.log(copiedEventObject)
            $.post("events/update/", {
                    // date: "date",
                    title: copiedEventObject.title,
                    start: copiedEventObject.start.toJSON(),
                },
                function() {
                    console.log("OK")
                }
            )
        },
        // 日历内拖动事件
        eventDrop: function(event, delta, revertFunc) {
            // alert(event.title + " was dropped on " + event.start.format());
            console.log(event.title + " was dropped on " + event.start.format());

            // if (!confirm("Are you sure about this change?")) {
            //     revertFunc();
            // }


        }
    });
});
