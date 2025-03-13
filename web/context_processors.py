def user_context(request):
    return {
        "user_department": request.user.department.id if hasattr(request.user, "department") else None
    }
