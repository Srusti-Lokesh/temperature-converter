from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ABSOLUTE_ZERO_C = -273.15
ABSOLUTE_ZERO_F = -459.67


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def celsius_to_kelvin(celsius):
    return celsius + 273.15


def kelvin_to_celsius(kelvin):
    return kelvin - 273.15


def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5 / 9 + 273.15


def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9 / 5 + 32


def convert_temperature(value, from_unit, to_unit):
    """Convert a temperature between C, F, and K with physical validation."""
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    if from_unit == "K" and value < 0:
        raise ValueError("Kelvin temperature cannot be below 0 K.")
    if from_unit == "C" and value < ABSOLUTE_ZERO_C:
        raise ValueError("Celsius temperature cannot be below -273.15 °C.")
    if from_unit == "F" and value < ABSOLUTE_ZERO_F:
        raise ValueError("Fahrenheit temperature cannot be below -459.67 °F.")

    if from_unit == to_unit:
        return value

    if from_unit == "C":
        if to_unit == "F":
            return celsius_to_fahrenheit(value)
        if to_unit == "K":
            return celsius_to_kelvin(value)

    if from_unit == "F":
        if to_unit == "C":
            return fahrenheit_to_celsius(value)
        if to_unit == "K":
            return fahrenheit_to_kelvin(value)

    if from_unit == "K":
        if to_unit == "C":
            return kelvin_to_celsius(value)
        if to_unit == "F":
            return kelvin_to_fahrenheit(value)

    raise ValueError("Units must be C, F, or K.")


@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    value = ""
    from_unit = "C"
    to_unit = "F"

    if request.method == "POST":
        value = request.form.get("value", "").strip()
        from_unit = request.form.get("from_unit", "C").upper()
        to_unit = request.form.get("to_unit", "F").upper()

        try:
            number = float(value)
            result = convert_temperature(number, from_unit, to_unit)
        except ValueError as exc:
            error = str(exc) if str(exc) else "Please enter a valid number."

    return render_template(
        "index.html",
        result=result,
        error=error,
        value=value,
        from_unit=from_unit,
        to_unit=to_unit,
    )


@app.route("/api/convert", methods=["GET"])
def api_convert():
    """Simple JSON endpoint for testing or API use."""
    try:
        value = float(request.args["value"])
        from_unit = request.args["from"].upper()
        to_unit = request.args["to"].upper()
        result = convert_temperature(value, from_unit, to_unit)
        return jsonify({
            "input": value,
            "from": from_unit,
            "to": to_unit,
            "result": round(result, 2)
        })
    except (KeyError, TypeError, ValueError) as exc:
        return jsonify({"error": str(exc) or "Invalid input."}), 400


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
