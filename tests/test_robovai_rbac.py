import pytest
import jwt
from robovai_rbac import RBACManager

def test_rbac_permissions():
    rbac = RBACManager(secret_key="test-secret")
    rbac.add_role("admin", ["docs:create", "docs:delete"])
    rbac.add_role("editor", ["docs:create"])
    rbac.add_role("superuser", ["*"])

    assert rbac.check_permission("admin", "docs:create") is True
    assert rbac.check_permission("admin", "docs:delete") is True
    assert rbac.check_permission("editor", "docs:delete") is False
    assert rbac.check_permission("superuser", "server:restart") is True

def test_decode_token():
    rbac = RBACManager(secret_key="test-secret")
    token = jwt.encode({"sub": "user123", "role": "admin"}, "test-secret", algorithm="HS256")
    decoded = rbac.decode_token(token)
    assert decoded["sub"] == "user123"
    assert decoded["role"] == "admin"
