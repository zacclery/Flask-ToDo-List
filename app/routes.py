from app import app, db
from app.models import Task
from flask import Flask, flash, redirect, render_template, request


@app.route('/')
@app.route('/index')
def tasks_list():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)


@app.route('/task', methods=['POST'])
def add_task():
    content = request.form['content']
    if not content:
        flash('Please enter text for your task')
        return redirect('/')
    task = Task(content)
    db.session.add(task)
    db.session.commit()
    return redirect('/')


@app.route('/toggle', methods=['POST'])
def toggle_status():
    task_id = request.form['task_id']
    task = Task.query.get(task_id)
    task.done = not task.done
    db.session.commit()
    return redirect('/')


@app.route('/edit', methods=['POST'])
def edit_task():
        task_id = request.form['task_id']
        edit_text = request.form['edit_text']
        if not edit_text:
            flash('Please enter text for your task')
            return redirect('/')
        task = Task.query.get(task_id)
        task.content = edit_text
        db.session.commit()
        return redirect('/')


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect('/')


@app.route('/finished')
def resolve_tasks():
    tasks = Task.query.all()
    for task in tasks:
        if not task:
            return redirect('/')
        if not task.done:
            task.done = True
        db.session.commit()
    return redirect('/')
