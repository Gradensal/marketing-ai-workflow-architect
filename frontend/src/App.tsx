import {
  useState,
} from "react";

import gradensalLogo from "./assets/gradensal-logo.png";

import WorkflowForm from "./components/WorkflowForm";

import {
  AnalysisApiError,
  analyzeWorkflow,
} from "./services/analysisApi";

import type {
  WorkflowAnalysis,
} from "./types/analysis";

import type {
  WorkflowInput,
} from "./types/workflow";

import "./styles/app.css";
import "./styles/analysis.css";


function formatRecommendation(
  recommendation: string,
) {
  const labels: Record<string, string> = {
    deterministic_automation:
      "DETERMINISTIC AUTOMATION",

    llm_assisted_workflow:
      "LLM-ASSISTED WORKFLOW",

    agentic_workflow:
      "AGENTIC WORKFLOW",

    keep_human_redesign_first:
      "KEEP HUMAN / REDESIGN FIRST",
  };


  return (
    labels[recommendation] ??
    recommendation
      .replaceAll("_", " ")
      .toUpperCase()
  );
}


function formatRisk(
  risk: string,
) {
  return risk.toUpperCase();
}


function App() {
  const [
    submittedWorkflow,
    setSubmittedWorkflow,
  ] = useState<WorkflowInput | null>(
    null,
  );

  const [
    analysis,
    setAnalysis,
  ] = useState<WorkflowAnalysis | null>(
    null,
  );

  const [
    isAnalyzing,
    setIsAnalyzing,
  ] = useState(false);

  const [
    error,
    setError,
  ] = useState<string | null>(
    null,
  );


  async function handleAnalyze(
    workflow: WorkflowInput,
  ) {
    setSubmittedWorkflow(workflow);

    setAnalysis(null);
    setError(null);
    setIsAnalyzing(true);


    try {
      const result =
        await analyzeWorkflow(workflow);

      setAnalysis(result);
    } catch (caughtError) {
      if (
        caughtError instanceof AnalysisApiError
      ) {
        setError(caughtError.message);
      } else if (
        caughtError instanceof Error
      ) {
        setError(caughtError.message);
      } else {
        setError(
          "Something unexpected happened while analyzing the workflow.",
        );
      }
    } finally {
      setIsAnalyzing(false);
    }
  }


  return (
    <div className="app-shell">
      <header className="brand-header">
        <div className="brand-identity">
          <img
            className="brand-logo"
            src={gradensalLogo}
            alt="Gradensal"
          />

          <div className="brand-wordmark">
            <span className="brand-name">
              GRADENSAL
            </span>

            <span className="brand-subtitle">
              SIGNATURE BUILDS
            </span>
          </div>
        </div>


        <div className="header-meta">
          <span className="system-status">
            <span
              className="system-status-dot"
              aria-hidden="true"
            />

            ARCHITECTURE DECISION SYSTEM
          </span>

          <div className="build-badge">
            GSB-002
          </div>
        </div>
      </header>


      <main>
        <section className="hero">
          <div className="hero-copy">
            <p className="eyebrow">
              MARKETING AI WORKFLOW ARCHITECT
            </p>

            <h1 className="hero-title">
              Choose the right level of AI

              <span className="hero-title-accent">
                before you build.
              </span>
            </h1>

            <p className="hero-description">
              Evaluate a business workflow through
              explicit, testable architecture rules.
              Then use AI to translate the recommendation
              into guidance a marketing team can actually use.
            </p>

            <div className="hero-principle">
              <span className="principle-dot" />

              Deterministic decision first.
              Generative explanation second.
            </div>
          </div>


          <div
            className="hero-art"
            aria-hidden="true"
          >
            <img
              className="hero-logo"
              src={gradensalLogo}
              alt=""
            />
          </div>
        </section>


        <section className="workspace">
          <article className="workspace-panel">
            <p className="panel-label">
              01 / WORKFLOW
            </p>

            <h2 className="panel-title">
              Describe the work
            </h2>

            <p className="panel-description">
              Capture the characteristics that determine
              whether this workflow needs traditional
              automation, LLM assistance, agentic behavior,
              or human-first design.
            </p>

            <WorkflowForm
              onAnalyze={handleAnalyze}
              isAnalyzing={isAnalyzing}
            />
          </article>


          <article className="workspace-panel">
            <p className="panel-label">
              02 / ANALYSIS
            </p>

            <h2 className="panel-title">
              Architecture recommendation
            </h2>

            <p className="panel-description">
              The deterministic assessment and AI
              explanation remain visibly separated so
              you can see which layer produced each part
              of the recommendation.
            </p>


            {isAnalyzing && (
              <div className="analysis-loading">
                <div
                  className="analysis-spinner"
                  aria-hidden="true"
                />

                <p className="analysis-loading-label">
                  ANALYZING WORKFLOW
                </p>

                <h3>
                  Selecting the architecture first.
                </h3>

                <p>
                  The deterministic engine evaluates
                  workflow characteristics before the
                  generative explanation layer is used.
                </p>
              </div>
            )}


            {!isAnalyzing &&
              error && (
                <div
                  className="analysis-error"
                  role="alert"
                >
                  <p className="analysis-error-label">
                    ANALYSIS FAILED
                  </p>

                  <h3>
                    We couldn't complete this analysis.
                  </h3>

                  <p>
                    {error}
                  </p>

                  <small>
                    Your workflow remains in the browser.
                    Verify that the FastAPI server is
                    running and then try again.
                  </small>
                </div>
              )}


            {!isAnalyzing &&
              !error &&
              analysis && (
                <div className="analysis-results">
                  <section className="assessment-card">
                    <div className="result-section-heading">
                      <span>
                        DETERMINISTIC ASSESSMENT
                      </span>

                      <span className="result-source-badge">
                        RULE ENGINE
                      </span>
                    </div>


                    <div className="recommendation-block">
                      <p className="recommendation-kicker">
                        RECOMMENDED ARCHITECTURE
                      </p>

                      <h3 className="recommendation-title">
                        {formatRecommendation(
                          analysis.assessment.recommendation,
                        )}
                      </h3>
                    </div>


                    <div className="assessment-metrics">
                      <div>
                        <span>
                          Risk
                        </span>

                        <strong>
                          {formatRisk(
                            analysis.assessment.risk_level,
                          )}
                        </strong>
                      </div>

                      <div>
                        <span>
                          Decision strength
                        </span>

                        <strong>
                          {
                            analysis.assessment
                              .decision_strength
                          }
                          /5
                        </strong>
                      </div>

                      <div>
                        <span>
                          Human approval
                        </span>

                        <strong>
                          {
                            analysis.assessment
                              .human_approval_required
                              ? "Required"
                              : "Not required"
                          }
                        </strong>
                      </div>
                    </div>


                    {analysis.assessment
                      .human_approval_reason && (
                      <div className="approval-reason">
                        <span>
                          WHY HUMAN APPROVAL
                        </span>

                        <p>
                          {
                            analysis.assessment
                              .human_approval_reason
                          }
                        </p>
                      </div>
                    )}


                    <div className="rationale-block">
                      <p className="result-subheading">
                        Why the rules engine chose this
                      </p>

                      <ul>
                        {analysis.assessment.rationale.map(
                          (
                            reason,
                            index,
                          ) => (
                            <li
                              key={`${index}-${reason}`}
                            >
                              {reason}
                            </li>
                          ),
                        )}
                      </ul>
                    </div>


                    {analysis.assessment
                      .warnings.length > 0 && (
                      <div className="warning-block">
                        <p className="result-subheading">
                          Guardrails
                        </p>

                        <ul>
                          {analysis.assessment.warnings.map(
                            (
                              warning,
                              index,
                            ) => (
                              <li
                                key={`${index}-${warning}`}
                              >
                                {warning}
                              </li>
                            ),
                          )}
                        </ul>
                      </div>
                    )}
                  </section>


                  {analysis.explanation_status ===
                    "unavailable" && (
                    <section className="explanation-unavailable">
                      <div className="result-section-heading">
                        <span>
                          AI EXPLANATION
                        </span>

                        <span className="result-source-badge unavailable">
                          UNAVAILABLE
                        </span>
                      </div>

                      <div className="explanation-unavailable-icon">
                        i
                      </div>

                      <h3>
                        The architecture decision is still valid.
                      </h3>

                      <p>
                        {
                          analysis.explanation_message ??
                          "The deterministic architecture assessment completed successfully, but the AI explanation is temporarily unavailable."
                        }
                      </p>

                      <div className="authority-note">
                        <strong>
                          What this means
                        </strong>

                        <span>
                          The recommendation above was produced
                          by the deterministic rule engine and
                          does not depend on the generative
                          explanation service.
                        </span>
                      </div>
                    </section>
                  )}


                  {analysis.explanation_status ===
                    "available" &&
                    analysis.explanation && (
                    <section className="explanation-card">
                      <div className="result-section-heading">
                        <span>
                          AI EXPLANATION
                        </span>

                        <span className="result-source-badge ai">
                          GPT-6 LUNA
                        </span>
                      </div>


                      <div className="explanation-item">
                        <p>
                          WHY THIS APPROACH
                        </p>

                        <div>
                          {
                            analysis.explanation
                              .why_this_approach
                          }
                        </div>
                      </div>


                      <div className="explanation-item">
                        <p>
                          WHY NOT MORE AUTONOMY
                        </p>

                        <div>
                          {
                            analysis.explanation
                              .why_not_more_autonomy
                          }
                        </div>
                      </div>


                      <div className="explanation-item">
                        <p>
                          PROPOSED ARCHITECTURE
                        </p>

                        <div>
                          {
                            analysis.explanation
                              .proposed_architecture
                          }
                        </div>
                      </div>


                      <div className="explanation-item">
                        <p>
                          HUMAN CHECKPOINT
                        </p>

                        <div>
                          {
                            analysis.explanation
                              .human_checkpoint
                          }
                        </div>
                      </div>


                      <div className="explanation-grid">
                        <div className="explanation-item">
                          <p>
                            FIRST EXPERIMENT
                          </p>

                          <div>
                            {
                              analysis.explanation
                                .first_experiment
                            }
                          </div>
                        </div>


                        <div className="explanation-item">
                          <p>
                            SUCCESS METRIC
                          </p>

                          <div>
                            {
                              analysis.explanation
                                .success_metric
                            }
                          </div>
                        </div>
                      </div>
                    </section>
                  )}
                </div>
              )}


            {!isAnalyzing &&
              !error &&
              !analysis && (
                <div className="review-state">
                  <strong>
                    Awaiting workflow
                  </strong>

                  <p>
                    Complete the workflow intake and
                    analyze it to receive an architecture
                    assessment and AI explanation.
                  </p>

                  {submittedWorkflow && (
                    <div className="next-step-note">
                      Ready to analyze{" "}
                      <strong>
                        {submittedWorkflow.name}
                      </strong>
                      .
                    </div>
                  )}
                </div>
              )}
          </article>
        </section>
      </main>


      <footer className="product-footer">
        <div className="footer-brand">
          <img
            src={gradensalLogo}
            alt=""
            aria-hidden="true"
          />

          <div>
            <strong>
              Gradensal
            </strong>

            <span>
              Signature Build GSB-002
            </span>
          </div>
        </div>


        <div className="footer-copy">
          <span>
            Marketing AI Workflow Architect
          </span>

          <span className="footer-separator">
            /
          </span>

          <span>
            Prototype v0.1.0
          </span>

          <span className="footer-separator">
            /
          </span>

          <span>
            Lissette Gorrin Rodriguez
          </span>
        </div>
      </footer>
    </div>
  );
}


export default App;