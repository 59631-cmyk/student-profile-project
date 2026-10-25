# Student Profile Website — CI/CD Project

## 1. Introduction

This project demonstrates Continuous Integration and Continuous Delivery (CI/CD) using GitHub Actions. It contains a simple student profile website and automated workflows for testing, validating, packaging, and deploying the application.

## 2. Project Architecture

The project contains the following components:

- `src/index.html`: Website source code.
- `tests/test_site.py`: Automated test cases.
- `requirements.txt`: Python testing dependency.
- `.github/workflows/ci.yml`: Continuous Integration workflow.
- `.github/workflows/deploy.yml`: Deployment workflow.
- `build/`: Generated website package during workflow execution.

## 3. CI Workflow

The CI workflow is triggered by code pushes and Pull Requests targeting the main branch. It checks out the source code, sets up Python, installs dependencies, checks project files, performs a Python syntax check, executes automated tests, and prepares a release package.

The workflow reports success when the required steps pass. If a required step fails, the workflow reports failure.

## 4. Build and Packaging

Since this is a static HTML website, no compilation is required. The workflow packages the application by copying `src/index.html` into the `build` directory and checking that the output file exists and is not empty.

## 5. Pull Request Validation

Developers create feature branches and submit Pull Requests targeting the main branch. GitHub Actions runs the CI checks, allowing problems to be detected before merging. A team member reviews the changes and provides approval or requests corrections.

Repository rules can be configured to require successful CI checks before merging.

## 6. Deployment Workflow

The project uses GitHub Pages for hosting. The deployment workflow runs on pushes to the main branch or when manually triggered. It first installs dependencies, executes the automated tests, and packages the website. The deployment job runs only after successful validation and publishes the artifact to GitHub Pages.

This is a Continuous Delivery configuration with automatic publishing after successful validation. A separate manual production approval is not configured.

## 7. Security Configuration

The workflows use limited permissions. The CI workflow has read-only repository access. The deployment job receives Pages write permission and OIDC token permission, while the deployment action handles authentication.

No passwords, API keys, or personal access tokens are stored in the workflow files. Third-party actions are referenced using version tags and should be reviewed and updated when necessary.

## 8. Testing

The automated tests verify that:

1. The homepage exists.
2. The correct page title is present.
3. Required student information is displayed.
4. Basic HTML structure is present.

A successful CI run demonstrates that these checks pass. A separate failed-test experiment should be performed and documented.

## 9. Deployment Verification

After successful deployment, the GitHub Pages URL is opened in a browser to verify that the student profile website loads correctly.

The actual repository URL, successful test evidence, failed-test evidence, Pull Request review, deployment workflow results, and published website URL should be attached to the final submission.

## 10. Conclusion

This project demonstrates an automated software delivery process using GitHub Actions. It integrates code validation, automated testing, packaging, Pull Request review, and deployment. The workflow reduces manual effort and helps identify errors before the website is published.