import type {
  CSSProperties,
} from "react";


type ScoreFieldProps = {
  label: string;

  description: string;

  value: number;

  lowLabel: string;

  highLabel: string;

  disabled?: boolean;

  onChange: (
    value: number,
  ) => void;
};


function ScoreField({
  label,
  description,
  value,
  lowLabel,
  highLabel,
  disabled = false,
  onChange,
}: ScoreFieldProps) {
  const progress =
    ((value - 1) / 4) * 100;


  const sliderStyle = {
    "--score-progress":
      `${progress}%`,
  } as CSSProperties;


  return (
    <div
      className={
        disabled
          ? "score-field score-field-disabled"
          : "score-field"
      }
    >
      <div className="score-field-header">
        <div>
          <label className="score-label">
            {label}
          </label>

          <p className="score-description">
            {description}
          </p>
        </div>


        <div
          className="score-value"
          aria-hidden="true"
        >
          {value}

          <span>
            /5
          </span>
        </div>
      </div>


      <input
        className="score-slider"
        type="range"
        min="1"
        max="5"
        step="1"
        value={value}
        disabled={disabled}
        style={sliderStyle}
        aria-label={label}
        aria-valuemin={1}
        aria-valuemax={5}
        aria-valuenow={value}
        aria-valuetext={
          `${value} out of 5. ` +
          `${lowLabel} to ${highLabel}.`
        }
        onChange={(event) =>
          onChange(
            Number(
              event.target.value,
            ),
          )
        }
      />


      <div
        className="score-scale"
        aria-hidden="true"
      >
        <span>
          {lowLabel}
        </span>


        <div className="score-markers">
          {[1, 2, 3, 4, 5].map(
            (score) => (
              <span
                key={score}
                className={
                  score === value
                    ? "score-marker score-marker-active"
                    : "score-marker"
                }
              >
                {score}
              </span>
            ),
          )}
        </div>


        <span>
          {highLabel}
        </span>
      </div>
    </div>
  );
}


export default ScoreField;