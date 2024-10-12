import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import cover
from esphome.const import (
    CONF_ADDRESS,
    CONF_ID,
    CONF_USE_ADDRESS,
    CONF_TX_PIN,
    CONF_RX_PIN,
)

CONF_UART_NUM = "uart_num"

bus_t4_ns = cg.esphome_ns.namespace('bus_t4')
Nice = bus_t4_ns.class_('NiceBusT4', cover.Cover, cg.Component)

CONFIG_SCHEMA = cover.COVER_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(Nice),
    cv.Optional(CONF_ADDRESS): cv.hex_uint16_t,
    cv.Optional(CONF_USE_ADDRESS): cv.hex_uint16_t,
    cv.Optional(CONF_TX_PIN): cv.int_range(min=0, max=39),
    cv.Optional(CONF_RX_PIN): cv.int_range(min=0, max=39),
    cv.Optional(CONF_UART_NUM): cv.one_of("UART_NUM_0", "UART_NUM_1", "UART_NUM_2", "UART0", upper=True),
}).extend(cv.COMPONENT_SCHEMA)


def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    yield cg.register_component(var, config)

    yield cover.register_cover(var, config)

    if CONF_ADDRESS in config:
        address = config[CONF_ADDRESS]
        cg.add(var.set_to_address(address))

    if CONF_USE_ADDRESS in config:
        use_address = config[CONF_USE_ADDRESS]
        cg.add(var.set_from_address(use_address))

    # Handle UART settings
    if CONF_TX_PIN in config:
        cg.add(var.set_tx_pin(config[CONF_TX_PIN]))
        
    if CONF_RX_PIN in config:
        cg.add(var.set_rx_pin(config[CONF_RX_PIN]))
        
    if CONF_UART_NUM in config:
        uart_num = config[CONF_UART_NUM]
        cg.add(var.set_uart_num(uart_num))
