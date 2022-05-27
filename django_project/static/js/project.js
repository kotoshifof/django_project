// 0文字以上はsubmitできない
$(function () {
  $("#todo-form-name").keyup(function (event) {
    // $(this.val().)
    console.log($(this).val());
    console.log($(this).val().trim().length);
    if ($(this).val().trim().length > 0  ) {
    $("#todo-form-submit").prop("disabled",false);
         }
    else {
    $("#todo-form-submit").prop("disabled",true);
         }

  })

//Add a new Todo
  $("#todo").submit(function (event) {
    const csrftoken = document.querySelector(
      "[name=csrfmiddlewaretoken]"
    ).value;
    console.log(csrftoken);
    console.log("token");
    $.ajax({
      type: "POST",
      url: "/todos/",
      headers: { "X-CSRFToken": csrftoken },
      data: {
        name: $("#todo-form-name").val(),
      },
      success: function (data) {
        console.log(data);
        const todo = data['todo']
        html = `
        <div id="todo${todo['id']}">
          <input type="checkbox"  class="todo-completed "></input>
          <input class="todo-name border-0" value="${todo["name"]}"></input>
        </div>
        `
        $("#todo_list").append(html);
        $("#id_name").val('')
      },
    });
  });
});
