from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj.creator or  #разрешено изменять, удалять авторам
                  request.user.is_superuser or      #разрешено изменять, удалять суперпользователям (администраторам)
                  request.method is SAFE_METHODS )  #всем разрешено использовать безопасные методы