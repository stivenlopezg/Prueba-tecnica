# Features
features = ['cupo_global', 'disponible', 'total_mes_en_mora', 'altura_de_mora', 'aumento_cupo',
            'SUM(trx.valor_transaccion)', 'SUM(trx.numero_cuotas_diferidas)', 'STD(trx.valor_transaccion)',
            'STD(trx.numero_cuotas_diferidas)', 'MAX(trx.valor_transaccion)', 'MAX(trx.numero_cuotas_diferidas)',
            'SKEW(trx.valor_transaccion)', 'SKEW(trx.numero_cuotas_diferidas)', 'MIN(trx.valor_transaccion)',
            'MIN(trx.numero_cuotas_diferidas)', 'MEAN(trx.valor_transaccion)', 'MEAN(trx.numero_cuotas_diferidas)',
            'COUNT(trx)', 'NUM_UNIQUE(trx.codigo_transaccion)', 'DAY(fecha_de_emision)', 'YEAR(fecha_de_emision)',
            'MONTH(fecha_de_emision)', 'WEEKDAY(fecha_de_emision)', 'NUM_UNIQUE(trx.MONTH(fecha_de_transaccion))',
            'NUM_UNIQUE(trx.WEEKDAY(fecha_de_transaccion))', 'NUM_UNIQUE(trx.DAY(fecha_de_transaccion))',
            'NUM_UNIQUE(trx.YEAR(fecha_de_transaccion))', 'MODE(trx.MONTH(fecha_de_transaccion))',
            'MODE(trx.WEEKDAY(fecha_de_transaccion))', 'MODE(trx.DAY(fecha_de_transaccion))',
            'MODE(trx.YEAR(fecha_de_transaccion))', 'franquicia_amex', 'franquicia_visa', 'franquicia_mastercard',
            'tipo_tarjeta_azul', 'tipo_tarjeta_clasica tradicional', 'tipo_tarjeta_oro', 'tipo_tarjeta_oro éxito',
            'tipo_tarjeta_platinum', 'tipo_tarjeta_verde', 'tipo_tarjeta_visa clasica', 'tipo_tarjeta_visa dorada',
            'tipo_tarjeta_visa platinum', 'tipo_tarjeta_clasica mastercard', 'tipo_tarjeta_e-card',
            'tipo_tarjeta_ideal',
            'tipo_tarjeta_mastercard clasica', 'tipo_tarjeta_mastercard platinum', 'tipo_tarjeta_mastercard virtual',
            'tipo_tarjeta_oro mastercard', 'tipo_tarjeta_oro tradicional', 'tipo_tarjeta_platinum mastercard']
target = 'codigo_estado_tarjeta'

# Continous and categorical features
categorical_features = ['franquicia', 'tipo_tarjeta']
numerical_features = ['cupo_global', 'disponible', 'total_mes_en_mora', 'altura_de_mora', 'aumento_cupo',
                      'SUM(trx.valor_transaccion)', 'SUM(trx.numero_cuotas_diferidas)', 'STD(trx.valor_transaccion)',
                      'STD(trx.numero_cuotas_diferidas)', 'MAX(trx.valor_transaccion)',
                      'MAX(trx.numero_cuotas_diferidas)',
                      'SKEW(trx.valor_transaccion)', 'SKEW(trx.numero_cuotas_diferidas)', 'MIN(trx.valor_transaccion)',
                      'MIN(trx.numero_cuotas_diferidas)', 'MEAN(trx.valor_transaccion)',
                      'MEAN(trx.numero_cuotas_diferidas)', 'COUNT(trx)', 'NUM_UNIQUE(trx.codigo_transaccion)',
                      'DAY(fecha_de_emision)', 'YEAR(fecha_de_emision)', 'MONTH(fecha_de_emision)',
                      'WEEKDAY(fecha_de_emision)', 'NUM_UNIQUE(trx.MONTH(fecha_de_transaccion))',
                      'NUM_UNIQUE(trx.WEEKDAY(fecha_de_transaccion))', 'NUM_UNIQUE(trx.DAY(fecha_de_transaccion))',
                      'NUM_UNIQUE(trx.YEAR(fecha_de_transaccion))', 'MODE(trx.MONTH(fecha_de_transaccion))',
                      'MODE(trx.WEEKDAY(fecha_de_transaccion))', 'MODE(trx.DAY(fecha_de_transaccion))',
                      'MODE(trx.YEAR(fecha_de_transaccion))']

# Categories for categorical features
franquicia_categories = ['amex', 'visa', 'mastercard']
tipo_tarjeta_categories = ['azul', 'clasica tradicional', 'mastercard platinum', 'platinum', 'verde', 'oro',
                           'visa clasica', 'visa dorada', 'oro éxito', 'visa platinum', 'oro tradicional',
                           'e-card', 'mastercard virtual', 'clasica mastercard', 'oro mastercard',
                           'ideal', 'mastercard clasica', 'platinum mastercard']
