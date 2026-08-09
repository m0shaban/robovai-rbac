# RoboVAI RBAC (`robovai-rbac`)

<div align="center">

[![PyPI version](https://img.shields.io/pypi/v/robovai-rbac.svg?style=flat-square&color=blue)](https://pypi.org/project/robovai-rbac/)
[![Python Versions](https://img.shields.io/pypi/pyversions/robovai-rbac.svg?style=flat-square)](https://pypi.org/project/robovai-rbac/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/badge/code%20style-ruff-000000.svg?style=flat-square)](https://github.com/astral-sh/ruff)
[![Type Checked: mypy](https://img.shields.io/badge/type%20checked-mypy-blue.svg?style=flat-square)](https://mypy-lang.org/)
[![Nesronix Ecosystem](https://img.shields.io/badge/Nesronix-Ecosystem-blueviolet.svg?style=flat-square)](https://nesronix.org)

**Enterprise Dynamic Role-Based Access Control (RBAC) & Authorization Middleware for Python APIs**

[Nesronix Community](https://nesronix.org) • [PyPI Package](https://pypi.org/project/robovai-rbac/) • [Author Portfolio](https://msalatmani.org)

</div>

---

## ⚡ Overview & Value Proposition

`robovai-rbac` is a production-ready, enterprise-grade Python library developed as part of the **Nesronix & RoboVAI** open-source AI infrastructure ecosystem.

Built with strict performance benchmarks, comprehensive type safety (`py.typed`), and zero unnecessary runtime dependencies, `robovai-rbac` enables developers to build scalable, resilient AI and backend applications with minimal boilerplate.

```
┌────────────────────────────────────────────────────────┐
│               Application Layer (FastAPI / Streamlit / CLI) │
└───────────────────────────┬────────────────────────────┘
                            │
              ▼───────────────────────────▼
              │      RoboVAI RBAC      │
              │  (Async-Ready • Type-Safe • Modular Core)│
              ▲───────────────────────────▲
                            │
┌───────────────────────────┴────────────────────────────┐
│      Production Infrastructure (Cloud / Docker / Edge)  │
└────────────────────────────────────────────────────────┘
```

---

## 🚀 Key Features

- **Dynamic Role & Permission Matrix**: Add, modify, and revoke granular permissions at runtime without restarts.
- **Stateless JWT Integration**: Embeds cryptographically signed permissions or roles directly in JWT payloads.
- **Framework Agnostic Decorators**: Seamlessly works with FastAPI, Flask, Django, Litestar, and vanilla Python functions.
- **Hierarchical Role Inheritance & Wildcards**: Support for `*` root access and granular action checking.
- **Fast & Lightweight**: Zero database queries required for token permission verification.

---

## 📦 Installation

Install the package directly from **PyPI**:

```bash
# Using pip
pip install robovai-rbac

# Using uv (High speed package manager)
uv add robovai-rbac

# Using poetry
poetry add robovai-rbac
```

---

## 💡 Quickstart

```python
from robovai_rbac import RBACManager

rbac = RBACManager(secret_key="my-super-secret-key")

# 1. Define roles and permissions
rbac.add_role("admin", ["users:read", "users:write", "analytics:view"])
rbac.add_role("viewer", ["users:read"])

# 2. Check permission for a role
has_write = rbac.check_permission("admin", "users:write")
print(f"Admin has write access: {has_write}")  # True

# Wildcard support
rbac.add_role("superuser", ["*"])
print(rbac.check_permission("superuser", "any:custom:action"))  # True
```

---

## 🛠️ Enterprise Architecture & Verification

All packages in the Nesronix ecosystem adhere to strict software quality assurance guidelines:

- **100% Type-Checked:** Complete PEP 561 compliance with `py.typed` embedded.
- **Automated CI/CD:** Cross-platform multi-Python matrix testing (Python 3.8 through 3.13) via GitHub Actions.
- **Modern Packaging:** Full PEP 517 / PEP 621 compliance (`pyproject.toml`).

---

## 🤝 Contributing

Contributions are welcome! Please read our [CONTRIBUTING.md](CONTRIBUTING.md) guide and submit pull requests to the main repository.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Run the Test Suite (`pytest`)
4. Commit your Changes (`git commit -m 'feat: Add some AmazingFeature'`)
5. Push to the Branch (`git push origin feature/AmazingFeature`)
6. Open a Pull Request

---

## 📄 License & Authors

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

- **Author & Architect:** [Mohamed Shaban (محمد شعبان العتماني)](https://github.com/m0shaban) — *Applied AI Engineer* ([msalatmani.org](https://msalatmani.org))
- **Community:** [Nesronix Community](https://nesronix.org) • [GitHub @Nesronix](https://github.com/Nesronix)
