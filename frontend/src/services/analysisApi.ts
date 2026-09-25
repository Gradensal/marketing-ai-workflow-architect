import type {
  WorkflowAnalysis,
} from "../types/analysis";

import type {
  WorkflowInput,
} from "../types/workflow";


const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL ??
  "http://127.0.0.1:8000";


export class AnalysisApiError extends Error {
  status: number;

  constructor(
    message: string,
    status: number,
  ) {
    super(message);

    this.name = "AnalysisApiError";
    this.status = status;
  }
}


export async function analyzeWorkflow(
  workflow: WorkflowInput,
): Promise<WorkflowAnalysis> {
  let response: Response;

  try {
    response = await fetch(
      `${API_BASE_URL}/api/v1/analyze`,
      {
        method: "POST",

        headers: {
          "Content-Type": "application/json",
        },

        body: JSON.stringify(workflow),
      },
    );
  } catch {
    throw new AnalysisApiError(
      "The analysis service could not be reached. Check that the FastAPI server is running.",
      0,
    );
  }


  if (!response.ok) {
    let message =
      `Workflow analysis failed with status ${response.status}.`;

    try {
      const errorBody = await response.json();

      if (
        typeof errorBody?.detail === "string"
      ) {
        message = errorBody.detail;
      } else if (
        Array.isArray(errorBody?.detail)
      ) {
        message =
          "The workflow data did not pass backend validation.";
      }
    } catch {
      // Keep the fallback message.
    }


    throw new AnalysisApiError(
      message,
      response.status,
    );
  }


  return response.json() as Promise<WorkflowAnalysis>;
}