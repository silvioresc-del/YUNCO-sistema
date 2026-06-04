/**
 * YUNCO — Configuración Central de Roles y Permisos
 * Archivo: yunco-permisos.js
 * 
 * IMPORTANTE: Solo contiene definición estática de roles y permisos.
 * No contiene lógica de negocio ni acceso a datos.
 * Para modificar permisos, editar SOLO este archivo.
 */

const YUNCO_PERMISOS = {

  // ── CLAVES DEFAULT ──────────────────────────────────────────
  CLAVES_DEFAULT: {
    '1':'1111','2':'2222','3':'3333','4':'4444','5':'5555',
    '6':'6666','7':'7777','8':'8888','9':'9999',
    'gerente':'gerente2024','dueno':'dueno2024','admin':'yunco2024'
  },

  // ── CLAVE MAESTRA ───────────────────────────────────────────
  CLAVE_MAESTRA_DEFAULT: 'SANTINO15',

  // ── MÁXIMO DE INTENTOS DE LOGIN ─────────────────────────────
  MAX_INTENTOS: 3,

  // ── TIEMPO DE INACTIVIDAD (minutos, 0 = sin límite) ─────────
  INACTIVIDAD_MIN: 0,

  // ── MÓDULOS VISIBLES POR ROL ────────────────────────────────
  // Controla qué botones aparecen en el menú principal (index.html)
  MODULOS: {
    vendedor: ['ventas.html','inventario.html'],
    gerente:  ['ventas.html','inventario.html','caja.html','reportes.html'],
    dueno:    ['ventas.html','inventario.html','caja.html','reportes.html'],
    admin:    ['inventario.html'],
  },

  // ── ACCESO A MÓDULOS POR URL ────────────────────────────────
  // Controla quién puede entrar a cada módulo aunque escriba la URL directamente
  ACCESO_URL: {
    'ventas.html':     ['vendedor','gerente','dueno'],
    'inventario.html': ['vendedor','gerente','dueno','admin'],
    'caja.html':       ['gerente','dueno'],
    'reportes.html':   ['gerente','dueno'],
  },

  // ── PERMISOS DENTRO DE VENTAS ───────────────────────────────
  VENTAS: {
    vendedor: {
      tabs:            ['nueva','presupuesto','consulta','clientes'],
      comprobantes:    ['A','B','NC','PRES'],
      verTodosComp:    false,
      eliminarComp:    false,
      config:          false,
      gestionUsuarios: false,
    },
    gerente: {
      tabs:            ['nueva','presupuesto','comprobantes','consulta','clientes'],
      comprobantes:    ['A','B','NC','ND','PRES'],
      verTodosComp:    true,
      eliminarComp:    true,
      config:          false,
      gestionUsuarios: false,
    },
    dueno: {
      tabs:            ['nueva','presupuesto','comprobantes','consulta','clientes','config'],
      comprobantes:    ['A','B','NC','ND','PRES'],
      verTodosComp:    true,
      eliminarComp:    true,
      config:          true,
      gestionUsuarios: true,
    },
    admin: {
      tabs:            ['nueva','presupuesto','comprobantes','consulta','clientes','config'],
      comprobantes:    ['A','B','NC','ND','PRES'],
      verTodosComp:    true,
      eliminarComp:    true,
      config:          true,
      gestionUsuarios: false,
    },
  },

  // ── PERMISOS DENTRO DE INVENTARIO ───────────────────────────
  INVENTARIO: {
    vendedor: {
      tabs:             ['consulta','alertas'],
      verCostos:        false,
      verPrecioVenta:   true,
      modificar:        false,
    },
    gerente: {
      tabs:             ['stock','entrada','salida','historial','alertas','consulta'],
      verCostos:        false,
      verPrecioVenta:   true,
      modificar:        true,
    },
    dueno: {
      tabs:             ['stock','entrada','salida','historial','alertas','consulta'],
      verCostos:        true,
      verPrecioVenta:   true,
      modificar:        true,
    },
    admin: {
      tabs:             ['consulta','alertas'],
      verCostos:        false,
      verPrecioVenta:   false,
      modificar:        false,
    },
  },

  // ── PERMISOS DENTRO DE CAJA ─────────────────────────────────
  CAJA: {
    gerente: {
      abrirCerrar:  true,
      verResumen:   true,
      verHistorial: true,
    },
    dueno: {
      abrirCerrar:  true,
      verResumen:   true,
      verHistorial: true,
    },
  },

  // ── ETIQUETAS DE ROLES ──────────────────────────────────────
  ETIQUETAS: {
    vendedor: 'Vendedor',
    gerente:  'Gerente General',
    dueno:    'Dueño',
    admin:    'Admin Técnico',
  },

  // ── HELPER: obtener permisos de ventas para un rol ──────────
  getVentas(rol){ return this.VENTAS[rol] || this.VENTAS['vendedor']; },

  // ── HELPER: obtener permisos de inventario para un rol ──────
  getInventario(rol){ return this.INVENTARIO[rol] || this.INVENTARIO['vendedor']; },

  // ── HELPER: verificar si rol puede acceder a módulo ─────────
  puedeAcceder(rol, modulo){ return (this.ACCESO_URL[modulo]||[]).includes(rol); },
};
