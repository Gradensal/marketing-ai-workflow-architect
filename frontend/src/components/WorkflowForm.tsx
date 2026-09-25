import {
  useState,
  type FormEvent,
} from "react";

import ScoreField from "./ScoreField";

import {
  EMPTY_WORKFLOW,
  SAMPLE_WORKFLOW,
  type WorkflowInput,
} from "../types/workflow";


type WorkflowFormProps = {
  onAnalyze: (
    workflow: WorkflowInput,
  ) => void | Promise<void>;

  isAnalyzing?: boolean;
};


function WorkflowForm({
  onAnalyze,
  isAnalyzing = false,
}: WorkflowFormProps) {
  const [
    workflow,
    setWorkflow,
  ] = useState<WorkflowInput>({
    ...EMPTY_WORKFLOW,
  });


  function updateField<
    K extends keyof WorkflowInput,
  >(
    field: K,
    value: WorkflowInput[K],
  ) {
    setWorkflow(
      (current) => ({
        ...current,
        [field]: value,
      }),
    );
  }


  async function handleSubmit(
    event: FormEvent<HTMLFormElement>,
  ) {
    event.preventDefault();

    if (
      isAnalyzing
    ) {
      return;
    }

    await onAnalyze(workflow);
  }


  function loadSample() {
    if (
      isAnalyzing
    ) {
      return;
    }

    setWorkflow({
      ...SAMPLE_WORKFLOW,
    });
  }


  function resetForm() {
    if (
      isAnalyzing
    ) {
      return;
    }

    setWorkflow({
      ...EMPTY_WORKFLOW,
    });
  }


  const canSubmit =
    workflow.name.trim().length >= 3 &&
    workflow.team.trim().length >= 2 &&
    workflow.description.trim().length >= 20;


  return (
    <form
      className="workflow-form"
      onSubmit={handleSubmit}
    >
      <div className="form-actions-top">
        <button
          className="text-button"
          type="button"
          disabled={isAnalyzing}
          onClick={loadSample}
        >
          Load example
        </button>

        <button
          className="text-button"
          type="button"
          disabled={isAnalyzing}
          onClick={resetForm}
        >
          Reset
        </button>
      </div>


      <div className="field-group">
        <label
          className="field-label"
          htmlFor="workflow-name"
        >
          Workflow name
        </label>

        <input
          id="workflow-name"
          className="text-input"
          type="text"
          value={workflow.name}
          placeholder="e.g. Weekly campaign reporting"
          minLength={3}
          maxLength={120}
          required
          disabled={isAnalyzing}
          onChange={(event) =>
            updateField(
              "name",
              event.target.value,
            )
          }
        />
      </div>


      <div className="field-group">
        <label
          className="field-label"
          htmlFor="workflow-team"
        >
          Team
        </label>

        <input
          id="workflow-team"
          className="text-input"
          type="text"
          value={workflow.team}
          placeholder="e.g. Marketing Operations"
          minLength={2}
          maxLength={80}
          required
          disabled={isAnalyzing}
          onChange={(event) =>
            updateField(
              "team",
              event.target.value,
            )
          }
        />
      </div>


      <div className="field-group">
        <div className="field-label-row">
          <label
            className="field-label"
            htmlFor="workflow-description"
          >
            Describe the workflow
          </label>

          <span className="field-hint">
            {workflow.description.length}
            /1500
          </span>
        </div>

        <textarea
          id="workflow-description"
          className="text-area"
          value={workflow.description}
          placeholder={
            "What happens today? " +
            "What information does the workflow use? " +
            "What actions does it take?"
          }
          minLength={20}
          maxLength={1500}
          required
          disabled={isAnalyzing}
          onChange={(event) =>
            updateField(
              "description",
              event.target.value,
            )
          }
        />
      </div>


      <div className="signal-section">
        <div className="signal-section-heading">
          <p className="signal-kicker">
            ARCHITECTURE SIGNALS
          </p>

          <h3>
            How does the workflow behave?
          </h3>

          <p>
            These characteristics help determine
            how much automation and autonomy the
            workflow actually needs.
          </p>
        </div>


        <ScoreField
          label="Repeatability"
          description={
            "How consistently does the workflow " +
            "follow the same sequence?"
          }
          value={workflow.repeatability}
          lowLabel="Changes often"
          highLabel="Highly repeatable"
          disabled={isAnalyzing}
          onChange={(value) =>
            updateField(
              "repeatability",
              value,
            )
          }
        />


        <ScoreField
          label="Ambiguity"
          description={
            "How much interpretation or judgment " +
            "is required?"
          }
          value={workflow.ambiguity}
          lowLabel="Clear rules"
          highLabel="High judgment"
          disabled={isAnalyzing}
          onChange={(value) =>
            updateField(
              "ambiguity",
              value,
            )
          }
        />


        <ScoreField
          label="Tool use"
          description={
            "How much does the workflow depend " +
            "on other systems or information sources?"
          }
          value={workflow.tool_use}
          lowLabel="Few tools"
          highLabel="Many systems"
          disabled={isAnalyzing}
          onChange={(value) =>
            updateField(
              "tool_use",
              value,
            )
          }
        />


        <ScoreField
          label="External actions"
          description={
            "How consequentially does the workflow " +
            "change or act on external systems?"
          }
          value={workflow.external_actions}
          lowLabel="Mostly read-only"
          highLabel="Acts externally"
          disabled={isAnalyzing}
          onChange={(value) =>
            updateField(
              "external_actions",
              value,
            )
          }
        />


        <ScoreField
          label="Business risk"
          description={
            "What could happen if the system " +
            "makes the wrong decision?"
          }
          value={workflow.business_risk}
          lowLabel="Minor impact"
          highLabel="Severe impact"
          disabled={isAnalyzing}
          onChange={(value) =>
            updateField(
              "business_risk",
              value,
            )
          }
        />


        <ScoreField
          label="Data sensitivity"
          description={
            "How sensitive is the information " +
            "handled by the workflow?"
          }
          value={workflow.data_sensitivity}
          lowLabel="Public / low"
          highLabel="Highly sensitive"
          disabled={isAnalyzing}
          onChange={(value) =>
            updateField(
              "data_sensitivity",
              value,
            )
          }
        />
      </div>


      <label className="approval-control">
        <input
          type="checkbox"
          checked={
            workflow.mandatory_human_approval
          }
          disabled={isAnalyzing}
          onChange={(event) =>
            updateField(
              "mandatory_human_approval",
              event.target.checked,
            )
          }
        />

        <span className="approval-box" />

        <span>
          <strong>
            Human approval is already mandatory
          </strong>

          <small>
            Enable this when policy or process
            requires a person to approve
            consequential actions.
          </small>
        </span>
      </label>


      <div className="form-footer">
        <p>
          Workflow characteristics are sent only
          to the local analysis API during this
          development build.
        </p>

        <button
          className="primary-button"
          type="submit"
          disabled={
            !canSubmit ||
            isAnalyzing
          }
        >
          {isAnalyzing
            ? "Analyzing..."
            : "Analyze workflow"}

          {!isAnalyzing && (
            <span aria-hidden="true">
              →
            </span>
          )}
        </button>
      </div>
    </form>
  );
}


export default WorkflowForm;