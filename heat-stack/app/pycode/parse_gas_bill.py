from rules_engine import (
    FuelType,
    HeatLoadInput,
    TemperatureInput,
    engine,
    parser,
)


def executeParse(csvDataJs):
    naturalGasInputRecords = parser.parse_gas_bill(csvDataJs)
    return naturalGasInputRecords.model_dump(mode="json")
