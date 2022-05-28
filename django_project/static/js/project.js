$(function () {
  // 0文字以上はsubmitできない
  $("#todo-form-name").keyup(function (event) {
    if ($(this).val().trim().length > 0  ) {
    $("#todo-form-submit").prop("disabled",false);
         }
    else {
    $("#todo-form-submit").prop("disabled",true);
         }
  })

  //Add a new Todo
  $("#todo").on('submit',function (event) {
    const csrftoken = document.querySelector(
      "[name=csrfmiddlewaretoken]"
    ).value;
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
        <div id="todo${todo['id']}" class="todo">
          <input type="checkbox" id="todo${todo['id']}-completed">
          <input id="todo${todo['id']}-name" class="border-0" value="${todo["name"]}">
         <button class="todo-delete-submit btn">
           <i class="fa fa-trash"></i>
         </button>
        </div>
        `
        $("#todo-list").append(html);
        $("#todo-form-name").val('')
        $("#todo-form-submit").prop("disabled",true);
      },
    });
  });

  // Delete
  $(document).on('click','.todo-delete-submit',function (event) {
    const csrftoken = document.querySelector(
      "[name=csrfmiddlewaretoken]"
    ).value;
    const todoId = $(this).parent().attr('id');
    $.ajax({
      type: "POST",
      url: "/todos/",
      headers: { "X-CSRFToken": csrftoken },
      data:
      {
      id: todoId.replace(/[^\d*]/g,''),
        method: 'DELETE',
      },
      success: function (data) {
        $(`#${todoId}`).remove();
        //notification message
      },
    });
  });

  // Update
  $(document).on('change','.todo',function (event) {
    const csrftoken = document.querySelector(
      "[name=csrfmiddlewaretoken]"
    ).value;
    const todoId = $(this).attr('id');
    const name = $(`#${todoId}-name`).val()
    const completed = $(`#${todoId}-completed`).prop('checked')
    $.ajax({
      type: "POST",
      url: "/todos/",
      headers: { "X-CSRFToken": csrftoken },
      data:
      {
      id: todoId.replace(/[^\d*]/g,''),
        name: name,
        completed: completed,
        method: 'UPDATE',
      },
      success: function (data) {
        //notification message
      },
    });
  });
});

