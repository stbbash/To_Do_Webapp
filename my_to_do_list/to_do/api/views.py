from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from to_do.models import Task
from .serializers import TaskSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint' : 'api',
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns an array of all the routes'
        },
        {
            'Endpoint' : 'api/user/create',  #CREATE
            'method' : 'POST',
            'body' : {'body' : ""},
            'description' : 'Creates new task with data sent in post request'
        },
        {
            'Endpoint' : 'api/user/',        #READ
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns an array of tasks from all users'
        },
        {
            'Endpoint' : 'api/user/user_id/',   #READ
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns an array of tasks from a specific user'
        },
        {
            'Endpoint' : 'api/user/user_id/id',     #READ
            'method' : 'GET',
            'body' : None,
            'description' : 'Returns a single task object from a specific user'
        },
        {
            'Endpoint' : 'api/user/user_id/id/update',      #UPDATE
            'method' : 'PUT',
            'body' : {'body' : ""},
            'description' : 'Updates a users existing task with data sent in put request'
        },
        {
            'Endpoint' : 'api/user/user_id/id/delete',      #DELETE
            'method' : 'delete',
            'body' : None,
            'description' : 'Deletes a users existing task'
        }
    ]
    return Response(routes)

#CREATE
@api_view(['POST'])
def createTask(request):
    data = request.data
    task = Task.objects.create(
        user_id = data['user_id'],
        title=data['title'],
        description=data['description'],
        complete=data['complete']
    )
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


#READ
@api_view(['GET'])
def users(request):
    task = Task.objects.all()
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)
    

#READ
@api_view(['GET'])
def userTasks(request, fk):
    task = Task.objects.filter(user_id=fk)
    serializer = TaskSerializer(task, many=True)
    return Response(serializer.data)
    

#READ
@api_view(['GET'])
def getTask(request, fk, pk):
    task = Task.objects.get(user_id=fk, id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


#UPDATE
@api_view(['PUT'])
def updateTask(request, fk, pk):
    data = request.data
    task = Task.objects.get(user_id=fk, id=pk)
    serializer = TaskSerializer(task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#DELETE
@api_view(['DELETE'])
def deleteTask(request, fk, pk):
    task = Task.objects.get(user_id=fk, id=pk)
    task.delete()
    return Response('Task was Deleted!')



