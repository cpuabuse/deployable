# Structure

## Pipeline

```mermaid
graph TB
	subgraph git[Git]
		subgraph git_deploy[py-deployment-automation]
			git_deploy_package[Python package]
		end
	end

	subgraph pipeline[Pipeline]
		pipeline_deploy[Deploy]
	end

	subgraph pypi[PyPI]
		pypi_package[deployment-automation]
	end

	%% Pipeline
	pipeline_deploy -- Use --> git_deploy_package
	pipeline_deploy == Publish ==> pypi_package
```

## Classes

```mermaid
classDiagram
	class Environment{
	}
	class Deployment{
	}
	class Stage{
	}

	Deployment "1..*" --* "1" Environment : composes
	Stage "1..*" --* "1" Deployment : composes
```
