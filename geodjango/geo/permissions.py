from rest_framework import permissions


class UserInGamePermission(permissions.BasePermission):
    message = "This user can not change this game"

    def has_permission(self, request, view, game):
        if request.method in ('PUT', 'PATCH'):
            return request.user.risk_profile in game.users
        return True
