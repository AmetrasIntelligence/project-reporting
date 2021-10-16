import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo11-addons-oca-project-reporting",
    description="Meta package for oca-project-reporting Odoo addons",
    version=version,
    install_requires=[
        'odoo11-addon-project_task_report',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 11.0',
    ]
)
