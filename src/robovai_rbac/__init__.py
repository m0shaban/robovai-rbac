"""
robovai-rbac: Enterprise Dynamic Role-Based Access Control (RBAC) & Auth Middleware.
Author: Mohamed Shaban (msalatmani@gmail.com)
"""

from .rbac import RBACManager, require_permission

__version__ = "0.1.0"
__author__ = "Mohamed Shaban"
__all__ = ["RBACManager", "require_permission"]
