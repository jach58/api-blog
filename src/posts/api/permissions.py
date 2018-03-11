from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrReadOnly(BasePermission):
    message = 'You must be Owner of this object'
    # my_safe_method = ['GET','PUT']
    #
    # def has_permissions(self,request,view):
    #     if request.method in self.my_safe_method:
    #         return True
    #     return False

    def has_object_permission(self, request, view, obj):
        #Permisos mas fuertes como saber si es miembro activo, etc
        # member =  Membership.objects.get(user = request.user)
        #member.is_active
        if request.method in SAFE_METHODS:
            return True
        return obj.user ==request.user