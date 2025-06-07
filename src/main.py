from __future__ import annotations

import argparse
from crewai import Agent, Task, Crew, Process

from .tools import ListTestFilesTool, ReadFileTool
from .analyzer import AzureTestReviewTool


def build_crew(directory: str) -> Crew:
    list_tool = ListTestFilesTool()
    read_tool = ReadFileTool()
    review_tool = AzureTestReviewTool()

    finder = Agent(
        role="Test Finder",
        goal="Identify python test files",
        backstory=(
            "Experienced developer who knows how to navigate project structures to"
            " locate test scripts."
        ),
        tools=[list_tool],
    )

    reviewer = Agent(
        role="Test Reviewer",
        goal="Check test code quality using Azure OpenAI",
        backstory=(
            "Seasoned QA engineer with knowledge of testing best practices and AI analysis."
        ),
        tools=[read_tool, review_tool],
    )

    collect = Task(
        description="List all python test files in {directory}",
        expected_output="A list of file paths",
        agent=finder,
    )

    analyze = Task(
        description=(
            "Read each file returned by the previous task and provide a quality review"
        ),
        expected_output="A markdown report with feedback for each file",
        agent=reviewer,
        context=[collect],
    )

    crew = Crew(
        agents=[finder, reviewer],
        tasks=[collect, analyze],
        process=Process.sequential,
        verbose=True,
    )
    return crew


def main() -> None:
    parser = argparse.ArgumentParser(description="Analyze python test quality")
    parser.add_argument("directory", help="Project directory to inspect")
    args = parser.parse_args()

    crew = build_crew(args.directory)
    result = crew.kickoff({"directory": args.directory})
    print(result)


if __name__ == "__main__":
    main()
