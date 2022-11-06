from rest_framework import viewsets, mixins


class ListDestroyCreateViewSet(mixins.CreateModelMixin,
                               mixins.ListModelMixin,
                               mixins.DestroyModelMixin,
                               viewsets.GenericViewSet):
    '''Создали собственный вьюсет, для класса подписок,'''
    '''для более удобной реализации определенных'''
    '''ограничений по ТЗ'''
    pass
