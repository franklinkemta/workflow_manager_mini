"""
Main module of our API
"""

# Config modules
from shared.config import app

# Routes Modules
from routes import IndexRoutes, WorkflowRoutes, ImageRoutes, ProgressionRoutes

# Run APP
if __name__ == "__main__":
    app.run(debug=True)