-- phpMyAdmin SQL Dump
-- version 4.8.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 11-02-2022 a las 23:41:47
-- Versión del servidor: 10.1.32-MariaDB
-- Versión de PHP: 7.2.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `encarpc_pagina`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint(20) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) COLLATE latin1_spanish_ci NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add ciudad', 7, 'add_ciudad'),
(26, 'Can change ciudad', 7, 'change_ciudad'),
(27, 'Can delete ciudad', 7, 'delete_ciudad'),
(28, 'Can view ciudad', 7, 'view_ciudad'),
(29, 'Can add cliente', 8, 'add_cliente'),
(30, 'Can change cliente', 8, 'change_cliente'),
(31, 'Can delete cliente', 8, 'delete_cliente'),
(32, 'Can view cliente', 8, 'view_cliente'),
(33, 'Can add departamento', 9, 'add_departamento'),
(34, 'Can change departamento', 9, 'change_departamento'),
(35, 'Can delete departamento', 9, 'delete_departamento'),
(36, 'Can view departamento', 9, 'view_departamento'),
(37, 'Can add nacionalidad', 10, 'add_nacionalidad'),
(38, 'Can change nacionalidad', 10, 'change_nacionalidad'),
(39, 'Can delete nacionalidad', 10, 'delete_nacionalidad'),
(40, 'Can view nacionalidad', 10, 'view_nacionalidad'),
(41, 'Can add proveedor', 11, 'add_proveedor'),
(42, 'Can change proveedor', 11, 'change_proveedor'),
(43, 'Can delete proveedor', 11, 'delete_proveedor'),
(44, 'Can view proveedor', 11, 'view_proveedor'),
(45, 'Can add usuario', 12, 'add_usuario'),
(46, 'Can change usuario', 12, 'change_usuario'),
(47, 'Can delete usuario', 12, 'delete_usuario'),
(48, 'Can view usuario', 12, 'view_usuario'),
(49, 'Can add reparacion', 13, 'add_reparacion'),
(50, 'Can change reparacion', 13, 'change_reparacion'),
(51, 'Can delete reparacion', 13, 'delete_reparacion'),
(52, 'Can view reparacion', 13, 'view_reparacion'),
(53, 'Can add perifericos', 14, 'add_perifericos'),
(54, 'Can change perifericos', 14, 'change_perifericos'),
(55, 'Can delete perifericos', 14, 'delete_perifericos'),
(56, 'Can view perifericos', 14, 'view_perifericos'),
(57, 'Can add mantenimiento', 15, 'add_mantenimiento'),
(58, 'Can change mantenimiento', 15, 'change_mantenimiento'),
(59, 'Can delete mantenimiento', 15, 'delete_mantenimiento'),
(60, 'Can view mantenimiento', 15, 'view_mantenimiento'),
(61, 'Can add tipo_ cpu', 16, 'add_tipo_cpu'),
(62, 'Can change tipo_ cpu', 16, 'change_tipo_cpu'),
(63, 'Can delete tipo_ cpu', 16, 'delete_tipo_cpu'),
(64, 'Can view tipo_ cpu', 16, 'view_tipo_cpu'),
(65, 'Can add tipo_ gabinete', 17, 'add_tipo_gabinete'),
(66, 'Can change tipo_ gabinete', 17, 'change_tipo_gabinete'),
(67, 'Can delete tipo_ gabinete', 17, 'delete_tipo_gabinete'),
(68, 'Can view tipo_ gabinete', 17, 'view_tipo_gabinete'),
(69, 'Can add tipo_ ram', 18, 'add_tipo_ram'),
(70, 'Can change tipo_ ram', 18, 'change_tipo_ram'),
(71, 'Can delete tipo_ ram', 18, 'delete_tipo_ram'),
(72, 'Can view tipo_ ram', 18, 'view_tipo_ram'),
(73, 'Can add repuestos', 19, 'add_repuestos'),
(74, 'Can change repuestos', 19, 'change_repuestos'),
(75, 'Can delete repuestos', 19, 'delete_repuestos'),
(76, 'Can view repuestos', 19, 'view_repuestos'),
(77, 'Can add ram', 20, 'add_ram'),
(78, 'Can change ram', 20, 'change_ram'),
(79, 'Can delete ram', 20, 'delete_ram'),
(80, 'Can view ram', 20, 'view_ram'),
(81, 'Can add placa_base', 21, 'add_placa_base'),
(82, 'Can change placa_base', 21, 'change_placa_base'),
(83, 'Can delete placa_base', 21, 'delete_placa_base'),
(84, 'Can view placa_base', 21, 'view_placa_base'),
(85, 'Can add cpu', 22, 'add_cpu'),
(86, 'Can change cpu', 22, 'change_cpu'),
(87, 'Can delete cpu', 22, 'delete_cpu'),
(88, 'Can view cpu', 22, 'view_cpu'),
(89, 'Can add gabinete', 23, 'add_gabinete'),
(90, 'Can change gabinete', 23, 'change_gabinete'),
(91, 'Can delete gabinete', 23, 'delete_gabinete'),
(92, 'Can view gabinete', 23, 'view_gabinete'),
(93, 'Can add montaje', 24, 'add_montaje'),
(94, 'Can change montaje', 24, 'change_montaje'),
(95, 'Can delete montaje', 24, 'delete_montaje'),
(96, 'Can view montaje', 24, 'view_montaje');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) COLLATE latin1_spanish_ci NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) COLLATE latin1_spanish_ci NOT NULL,
  `first_name` varchar(150) COLLATE latin1_spanish_ci NOT NULL,
  `last_name` varchar(150) COLLATE latin1_spanish_ci NOT NULL,
  `email` varchar(254) COLLATE latin1_spanish_ci NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint(20) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext COLLATE latin1_spanish_ci,
  `object_repr` varchar(200) COLLATE latin1_spanish_ci NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext COLLATE latin1_spanish_ci NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) COLLATE latin1_spanish_ci NOT NULL,
  `model` varchar(100) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(7, 'Pagina', 'ciudad'),
(8, 'Pagina', 'cliente'),
(22, 'Pagina', 'cpu'),
(9, 'Pagina', 'departamento'),
(23, 'Pagina', 'gabinete'),
(15, 'Pagina', 'mantenimiento'),
(24, 'Pagina', 'montaje'),
(10, 'Pagina', 'nacionalidad'),
(14, 'Pagina', 'perifericos'),
(21, 'Pagina', 'placa_base'),
(11, 'Pagina', 'proveedor'),
(20, 'Pagina', 'ram'),
(13, 'Pagina', 'reparacion'),
(19, 'Pagina', 'repuestos'),
(16, 'Pagina', 'tipo_cpu'),
(17, 'Pagina', 'tipo_gabinete'),
(18, 'Pagina', 'tipo_ram'),
(12, 'Pagina', 'usuario'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint(20) NOT NULL,
  `app` varchar(255) COLLATE latin1_spanish_ci NOT NULL,
  `name` varchar(255) COLLATE latin1_spanish_ci NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'Pagina', '0001_initial', '2022-02-03 23:29:10.319549'),
(2, 'contenttypes', '0001_initial', '2022-02-03 23:29:10.375733'),
(3, 'auth', '0001_initial', '2022-02-03 23:29:11.100006'),
(4, 'admin', '0001_initial', '2022-02-03 23:29:11.242366'),
(5, 'admin', '0002_logentry_remove_auto_add', '2022-02-03 23:29:11.252309'),
(6, 'admin', '0003_logentry_add_action_flag_choices', '2022-02-03 23:29:11.261468'),
(7, 'contenttypes', '0002_remove_content_type_name', '2022-02-03 23:29:11.351033'),
(8, 'auth', '0002_alter_permission_name_max_length', '2022-02-03 23:29:11.526398'),
(9, 'auth', '0003_alter_user_email_max_length', '2022-02-03 23:29:11.590697'),
(10, 'auth', '0004_alter_user_username_opts', '2022-02-03 23:29:11.600824'),
(11, 'auth', '0005_alter_user_last_login_null', '2022-02-03 23:29:11.648403'),
(12, 'auth', '0006_require_contenttypes_0002', '2022-02-03 23:29:11.653420'),
(13, 'auth', '0007_alter_validators_add_error_messages', '2022-02-03 23:29:11.663173'),
(14, 'auth', '0008_alter_user_username_max_length', '2022-02-03 23:29:11.732492'),
(15, 'auth', '0009_alter_user_last_name_max_length', '2022-02-03 23:29:11.810937'),
(16, 'auth', '0010_alter_group_name_max_length', '2022-02-03 23:29:11.886209'),
(17, 'auth', '0011_update_proxy_permissions', '2022-02-03 23:29:11.900297'),
(18, 'auth', '0012_alter_user_first_name_max_length', '2022-02-03 23:29:11.965781'),
(19, 'sessions', '0001_initial', '2022-02-03 23:29:12.014954'),
(20, 'Pagina', '0002_repuestos_tipo_cpu_tipo_gabinete_tipo_ram', '2022-02-04 03:11:27.212895'),
(21, 'Pagina', '0003_auto_20220204_0031', '2022-02-04 03:31:09.917676'),
(22, 'Pagina', '0002_ram', '2022-02-04 04:12:26.473437'),
(23, 'Pagina', '0003_auto_20220204_0120', '2022-02-04 04:20:19.607020'),
(24, 'Pagina', '0004_tipo_cpu_tipo_gabinete_tipo_ram', '2022-02-04 04:20:52.201383'),
(25, 'Pagina', '0005_auto_20220204_1834', '2022-02-04 21:34:56.722140'),
(26, 'Pagina', '0006_placa_base', '2022-02-04 22:30:26.147112'),
(27, 'Pagina', '0007_cpu_gabinete', '2022-02-05 01:05:29.152042'),
(28, 'Pagina', '0008_montaje', '2022-02-08 00:57:51.636701'),
(29, 'Pagina', '0009_rename_tipo_periferico_montaje_id_periferico', '2022-02-08 01:14:03.992146'),
(30, 'Pagina', '0010_rename_placa_base_montaje_id_placa_base', '2022-02-08 01:35:52.752534'),
(31, 'Pagina', '0011_rename_id_placa_base_montaje_placa_base', '2022-02-08 01:38:50.152568'),
(32, 'Pagina', '0012_rename_placa_base_montaje_id_placa_base', '2022-02-08 01:59:29.903418'),
(33, 'Pagina', '0013_rename_id_placa_base_montaje_placa_base', '2022-02-08 02:08:59.653182'),
(34, 'Pagina', '0014_rename_placa_base_montaje_placa', '2022-02-08 02:15:26.091137'),
(35, 'Pagina', '0015_rename_placa_montaje_placa_base', '2022-02-08 02:21:23.099917'),
(36, 'Pagina', '0016_rename_placa_base_montaje_id_placa_base', '2022-02-08 03:59:11.812155'),
(37, 'Pagina', '0017_auto_20220208_1553', '2022-02-08 18:53:25.806699');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) COLLATE latin1_spanish_ci NOT NULL,
  `session_data` longtext COLLATE latin1_spanish_ci NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('2afgtkas2n47fnh278jfn3rpibas7jno', '.eJyrVspMiS8tLk0sysxXsjI00lHKy89NKkqNT87PLchJLclHSCp5lSbmKXhnphblVaZW5VUq6SiVZBYgKTCsBQBmpRyM:1nEy8N:H8SjpzJf4DkzIB6ZsN8LQ0RbNlS2xMxFuWC-x7WteFA', '2022-02-15 18:44:07.434628'),
('4txgzo88o04pmezhcjod1vypqly4d2yo', '.eJyrVspMiS8tLk0sysxXsjI00lHKy89NKkqNT87PLchJLclHSCp5lSbmKXhnphblVaZW5VUq6SiVZBYgKTCsBQBmpRyM:1nEFjS:Gs4onH-MG0yIDxDwAcvkuoDVehkwxkucPBrWvBqxuRQ', '2022-02-13 19:19:26.285835'),
('5nnjiabrt52if0w8p99sjgl3dj4jjk37', '.eJyrVspMiS8tLk0sysxXsjI011HKy89NKkqNT87PLchJLclHSCoFJCbl5Cs4pealpmRWKOkolWQWIEkb1QIAJtobeQ:1nI80L:LIQ4w_B_Ar40I6biBSr0mVSwFixyaQ0R_Jaah2MMQ0c', '2022-02-24 11:52:53.186930'),
('7y6zq3yglw1tvasgjjq6mh0bc4cl7pou', '.eJyrVspMiS8tLk0sysxXsjI00lHKy89NKkqNT87PLchJLclHSCp5lSbmKXhnphblVaZW5VUq6SiVZBYgKTCsBQBmpRyM:1nFnCr:r7xptHqYBs4TkFWaDGMomNtBtXiH5NzNPa-8XgL3gsI', '2022-02-18 01:16:09.236830'),
('kjvxr0xhavsshpktdowferh9l5yzpzwt', '.eJyrVspMiS8tLk0sysxXsjLUUcrLz00qSo1Pzs8tyEktyUfIKXmVJuYpeGemFuVVplblVSrpKJVkFiApMKwFAFT4HFo:1mrqRN:8JADpIE8e4HDTlNArUjmTV40S0DEcydlwNC_jjVaz_Y', '2021-12-13 23:52:09.248067'),
('rwkf8sgeqspb6c3uu8y35xj9n6p044p3', '.eJyrVspMiS8tLk0sysxXsjLUUcrLz00qSo1Pzs8tyEktyUfIKXmVJuYpeGemFuVVplblVSrpKJVkFiApMKwFAFT4HFo:1mrPHP:mkgw_-iDCBnw_PKntqXD5a656fG9JaPWDEzLzH5J5Ko', '2021-12-12 18:52:03.109124'),
('v24srd2e9mkjbdb3077wnguv7n5k1kwk', '.eJyrVspMiS8tLk0sysxXsjI00FHKy89NKkqNT87PLchJLclHSCo55qRWKLhkphan5ijpKJVkFiBJGtUCAOyGGqU:1mq21I:Wn6fK2TAIH1SktVjyNZpTYH4cw_zQgWfFfM8thwxMVU', '2021-12-08 23:49:44.971163');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_ciudad`
--

CREATE TABLE `pagina_ciudad` (
  `codigo_ciudad` int(11) NOT NULL,
  `nombre_ciudad` varchar(100) COLLATE latin1_spanish_ci NOT NULL,
  `nombre_departamento_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_ciudad`
--

INSERT INTO `pagina_ciudad` (`codigo_ciudad`, `nombre_ciudad`, `nombre_departamento_id`) VALUES
(2, 'Encarnación', 1),
(4, 'Ciudad del Este', 4),
(5, 'Paraguari', 8),
(6, 'Obligado', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_cliente`
--

CREATE TABLE `pagina_cliente` (
  `codigo_cliente` int(11) NOT NULL,
  `nombre_cliente` varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  `ruc_cliente` varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  `telefono_cliente` varchar(30) COLLATE latin1_spanish_ci NOT NULL,
  `direccion_cliente` varchar(200) COLLATE latin1_spanish_ci NOT NULL,
  `genero_cliente` int(11) DEFAULT NULL,
  `descripcion_nacionalidad_id` int(11) DEFAULT NULL,
  `nombre_ciudad_id` int(11) DEFAULT NULL,
  `nombre_departamento_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_cliente`
--

INSERT INTO `pagina_cliente` (`codigo_cliente`, `nombre_cliente`, `ruc_cliente`, `telefono_cliente`, `direccion_cliente`, `genero_cliente`, `descripcion_nacionalidad_id`, `nombre_ciudad_id`, `nombre_departamento_id`) VALUES
(12, 'Alex Gustavo Diesel Morais', '4921160', '0985724716', 'Bo. El portal', 1, 1, 6, 1),
(13, 'Juan Kiernyezny', '5195110-0', '0981116134', 'Encarnacion', 1, 1, 2, 1),
(14, 'Yessica Paola Biruk Gerasinchuk', '5150760', '0983547603', 'Bo. San Nicolás', 2, 1, 2, 1),
(15, 'Pablo Benedix', '4883067', '0985963941', 'Bo. Parque', 1, 1, 6, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_cpu`
--

CREATE TABLE `pagina_cpu` (
  `id_cpu` int(11) NOT NULL,
  `cod_cpu` int(11) DEFAULT NULL,
  `marca_cpu` varchar(30) COLLATE latin1_spanish_ci NOT NULL,
  `descripcion_cpu` varchar(200) COLLATE latin1_spanish_ci NOT NULL,
  `precio_compra_cpu` int(11) NOT NULL,
  `precio_venta_cpu` int(11) NOT NULL,
  `stock_cpu` int(11) NOT NULL,
  `imagen_cpu` varchar(100) COLLATE latin1_spanish_ci DEFAULT NULL,
  `nombre_proveedor_id` int(11) DEFAULT NULL,
  `tipo_cpu_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_cpu`
--

INSERT INTO `pagina_cpu` (`id_cpu`, `cod_cpu`, `marca_cpu`, `descripcion_cpu`, `precio_compra_cpu`, `precio_venta_cpu`, `stock_cpu`, `imagen_cpu`, `nombre_proveedor_id`, `tipo_cpu_id`) VALUES
(1, 31126, 'Intel Core', 'i5 9500 / 3.0 GHz / 9MB', 1400000, 1707317, 3, 'cpu/538008.png', 5, 1),
(2, 31798, 'Intel Celeron', 'Celeron G6900 / 3.4GHz / 4MB', 608000, 741463, 2, 'cpu/540619.PNG', 5, 2),
(3, 29973, 'AMD', 'Ryzen Threadripper PRO 3955WX / 3.9GHz / 73MB', 8973250, 10942988, 3, 'cpu/532921', 5, 3);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_departamento`
--

CREATE TABLE `pagina_departamento` (
  `codigo_departamento` int(11) NOT NULL,
  `nombre_departamento` varchar(100) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_departamento`
--

INSERT INTO `pagina_departamento` (`codigo_departamento`, `nombre_departamento`) VALUES
(1, 'Itapúa'),
(2, 'Misiones'),
(3, 'Alto Paraguay'),
(4, 'Alto Paraná'),
(5, 'Boquerón'),
(6, 'Presidente Hayes'),
(7, 'Cordillera'),
(8, 'Paraguari'),
(9, 'Ñeembucú'),
(10, 'Central'),
(11, 'Guaira'),
(12, 'Caazapá'),
(13, 'Amambay'),
(14, 'Canindeyú'),
(15, 'Concepción'),
(16, 'San Pedro'),
(18, 'Caaguazú');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_gabinete`
--

CREATE TABLE `pagina_gabinete` (
  `id_gab` int(11) NOT NULL,
  `cod_gab` int(11) DEFAULT NULL,
  `marca_gab` varchar(30) COLLATE latin1_spanish_ci NOT NULL,
  `descripcion_gab` varchar(200) COLLATE latin1_spanish_ci NOT NULL,
  `precio_compra_gab` int(11) NOT NULL,
  `precio_venta_gab` int(11) NOT NULL,
  `stock_gab` int(11) NOT NULL,
  `imagen_gab` varchar(100) COLLATE latin1_spanish_ci DEFAULT NULL,
  `nombre_proveedor_id` int(11) DEFAULT NULL,
  `tipo_gabinete_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_gabinete`
--

INSERT INTO `pagina_gabinete` (`id_gab`, `cod_gab`, `marca_gab`, `descripcion_gab`, `precio_compra_gab`, `precio_venta_gab`, `stock_gab`, `imagen_gab`, `nombre_proveedor_id`, `tipo_gabinete_id`) VALUES
(1, 647359, 'Satellite', 'Gabinete Satellite 8103k', 260000, 317073, 4, 'gab/67_elhkbt.jpg', 6, 1),
(2, 666275, 'Cooler Master', 'Gabinete Cooler Master Masterbox MS600 - Blanco', 320000, 390244, 2, 'gab/78_ypybhy.jpg', 6, 2),
(3, 29665, 'NZXT', 'NZXT H710 Mid Tower / 4 Cooler - Black/Red', 1071785, 1307055, 2, 'gab/535749', 5, 1),
(4, 29633, 'Darkflash', 'Darkflash DLH 21', 571285, 696689, 2, 'gab/530188', 5, 2),
(5, 27570, 'AZZA', 'AZZA Cube Mini 805 / 1 Cooler', 1637350, 1996768, 1, 'gab/519470', 5, 1),
(6, 27571, 'AZZA', 'AZZA Pyramid Mini 806 / 1 Cooler / RGB', 1430000, 1743902, 1, 'gab/519472', 5, 2),
(7, 73770, 'Gamemax', 'Gamemax Autobot - Plata', 1474781, 1798513, 4, 'gab/73770-1.jpg', 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_mantenimiento`
--

CREATE TABLE `pagina_mantenimiento` (
  `codigo_mant` int(11) NOT NULL,
  `equipo_mant` int(11) DEFAULT NULL,
  `desc_equipo_mant` varchar(200) COLLATE latin1_spanish_ci NOT NULL,
  `horas_mant` int(11) DEFAULT NULL,
  `actividades_mant` varchar(200) COLLATE latin1_spanish_ci NOT NULL,
  `inicio_mant` date NOT NULL,
  `fin_mant` date NOT NULL,
  `estado_mant` int(11) DEFAULT NULL,
  `nombre_cliente_id` int(11) DEFAULT NULL,
  `nombre_completo_usuario_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_mantenimiento`
--

INSERT INTO `pagina_mantenimiento` (`codigo_mant`, `equipo_mant`, `desc_equipo_mant`, `horas_mant`, `actividades_mant`, `inicio_mant`, `fin_mant`, `estado_mant`, `nombre_cliente_id`, `nombre_completo_usuario_id`) VALUES
(6, 2, 'PS4 Fat', 1, 'Cambio de Pasta y Limpieza', '2022-01-01', '2022-01-01', 1, 13, 10),
(7, 1, 'R7 5700G', 2, 'Cambio de Pasta y Limpieza', '2022-02-05', '2022-02-05', 3, 15, 16),
(8, 3, 'PS3', 2, 'Cambio de Pasta y Limpieza', '2022-02-08', '2022-02-08', 2, 12, 16);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_montaje`
--

CREATE TABLE `pagina_montaje` (
  `codigo_montaje` int(11) NOT NULL,
  `horas_mont` int(11) DEFAULT NULL,
  `actividades_mont` varchar(200) COLLATE latin1_spanish_ci NOT NULL,
  `inicio_mont` date NOT NULL,
  `fin_mont` date NOT NULL,
  `estado_mont` int(11) DEFAULT NULL,
  `nombre_cliente_id` int(11) DEFAULT NULL,
  `nombre_completo_usuario_id` int(11) DEFAULT NULL,
  `id_placa_base_id` int(11) DEFAULT NULL,
  `tipo_cpu_id` int(11) DEFAULT NULL,
  `tipo_gabinete_id` int(11) DEFAULT NULL,
  `id_periferico_id` int(11) DEFAULT NULL,
  `tipo_ram_id` int(11) DEFAULT NULL,
  `tipo_almacenamiento` int(11) DEFAULT NULL,
  `tipo_fuente` int(11) DEFAULT NULL,
  `tipo_placa_video` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_montaje`
--

INSERT INTO `pagina_montaje` (`codigo_montaje`, `horas_mont`, `actividades_mont`, `inicio_mont`, `fin_mont`, `estado_mont`, `nombre_cliente_id`, `nombre_completo_usuario_id`, `id_placa_base_id`, `tipo_cpu_id`, `tipo_gabinete_id`, `id_periferico_id`, `tipo_ram_id`, `tipo_almacenamiento`, `tipo_fuente`, `tipo_placa_video`) VALUES
(2, 1, 'Montaje de PC Nueva', '2020-01-01', '2022-01-01', 3, 12, 12, 3, 2, 1, 17, 3, 0, 20, 21),
(3, 2, 'Montaje de PC Nueva', '2022-02-09', '2022-02-09', 3, 13, 16, 2, 1, 2, 18, 1, 22, 20, 21),
(4, 3, 'Montaje de PC Nueva', '2022-02-11', '2022-02-11', 3, 13, 16, 3, 2, 3, 18, 3, 22, 20, 23);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_nacionalidad`
--

CREATE TABLE `pagina_nacionalidad` (
  `codigo_nacionalidad` int(11) NOT NULL,
  `descripcion_nacionalidad` varchar(50) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_nacionalidad`
--

INSERT INTO `pagina_nacionalidad` (`codigo_nacionalidad`, `descripcion_nacionalidad`) VALUES
(1, 'Paraguaya'),
(2, 'Argentina'),
(3, 'Brasilera');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_perifericos`
--

CREATE TABLE `pagina_perifericos` (
  `id_periferico` int(11) NOT NULL,
  `cod_periferico` int(11) DEFAULT NULL,
  `tipo_periferico` int(11) DEFAULT NULL,
  `marca_periferico` varchar(30) COLLATE latin1_spanish_ci NOT NULL,
  `descripcion_periferico` varchar(200) COLLATE latin1_spanish_ci NOT NULL,
  `precio_compra_periferico` int(11) NOT NULL,
  `precio_venta_periferico` int(11) NOT NULL,
  `stock_periferico` int(11) NOT NULL,
  `imagen_periferico` varchar(100) COLLATE latin1_spanish_ci DEFAULT NULL,
  `nombre_proveedor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_perifericos`
--

INSERT INTO `pagina_perifericos` (`id_periferico`, `cod_periferico`, `tipo_periferico`, `marca_periferico`, `descripcion_periferico`, `precio_compra_periferico`, `precio_venta_periferico`, `stock_periferico`, `imagen_periferico`, `nombre_proveedor_id`) VALUES
(17, 63020, 4, 'Gamemax', 'M386B LED 3 CORES 3200DPI', 100000, 130000, 1, 'perifericos/M386-roxosize-1200-800_KUe9Jwl_pOVSE1r.png', 1),
(18, 736664, 6, 'Redragon', 'Redragon Pandora 2 H350RGB-1', 217000, 320000, 5, 'perifericos/71-kciti6vl._ac_sl1500__1__1_xmcffa.jpg', 6),
(19, 701419, 4, 'Logitech', 'Logitech G603 Wireless 12000DPI', 295000, 380000, 4, 'perifericos/27_riywvr.jpg', 6),
(20, 751612, 1, 'Aigo', 'Aigo G-T550 550W / 80Plus Bronze / Full Modular', 405000, 520000, 3, 'perifericos/cincocin_lmgehf.jpg', 6),
(21, 846813, 8, 'AFOX', 'Placa de Vídeo AFOX GT-750 2GB / GDDR5', 870000, 1150000, 2, 'perifericos/1.png', 6),
(22, 27000, 3, 'Kingston', 'SSD Kingston 240GB 2.5\" - SA400S37/240G', 215000, 290000, 3, 'perifericos/531511', 5),
(23, 31771, 8, 'GALAX', 'GALAX 1-Click OC 6GB GeForce GTX1660Ti GDDR6', 3853850, 4699817, 2, 'perifericos/540417', 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_placa_base`
--

CREATE TABLE `pagina_placa_base` (
  `id_placa_base` int(11) NOT NULL,
  `cod_placa_base` int(11) DEFAULT NULL,
  `marca_placa_base` varchar(30) COLLATE latin1_spanish_ci NOT NULL,
  `descripcion_placa_base` varchar(200) COLLATE latin1_spanish_ci NOT NULL,
  `precio_compra_placa_base` int(11) NOT NULL,
  `precio_venta_placa_base` int(11) NOT NULL,
  `stock_placa_base` int(11) NOT NULL,
  `imagen_placa_base` varchar(100) COLLATE latin1_spanish_ci DEFAULT NULL,
  `nombre_proveedor_id` int(11) DEFAULT NULL,
  `tipo_cpu_placa_base_id` int(11) DEFAULT NULL,
  `tipo_gabinete_placa_base_id` int(11) DEFAULT NULL,
  `tipo_ram_placa_base_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_placa_base`
--

INSERT INTO `pagina_placa_base` (`id_placa_base`, `cod_placa_base`, `marca_placa_base`, `descripcion_placa_base`, `precio_compra_placa_base`, `precio_venta_placa_base`, `stock_placa_base`, `imagen_placa_base`, `nombre_proveedor_id`, `tipo_cpu_placa_base_id`, `tipo_gabinete_placa_base_id`, `tipo_ram_placa_base_id`) VALUES
(2, 852180, 'Asrock', 'Asrock B365M', 315000, 420000, 1, 'placa_base/70_eL6Rs5N.png', 6, 1, 2, 4),
(3, 31513, 'MSI', 'MPG Z690 Carbon Wi-Fi', 3425000, 4000000, 2, 'placa_base/540230.PNG', 5, 2, 1, 5),
(4, 901590, 'Asus', 'Pro WS WRX80E-SAGE SE WIFI', 7856942, 9581637, 1, 'placa_base/Asus-Pro-WS-WRX80E-SAGE-SE-WIFI.jpg', 1, 3, 1, 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_proveedor`
--

CREATE TABLE `pagina_proveedor` (
  `codigo_proveedor` int(11) NOT NULL,
  `nombre_proveedor` varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  `razon_social_proveedor` varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  `ruc_proveedor` varchar(50) COLLATE latin1_spanish_ci NOT NULL,
  `telefono_proveedor` varchar(30) COLLATE latin1_spanish_ci NOT NULL,
  `direccion_proveedor` varchar(200) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_proveedor`
--

INSERT INTO `pagina_proveedor` (`codigo_proveedor`, `nombre_proveedor`, `razon_social_proveedor`, `ruc_proveedor`, `telefono_proveedor`, `direccion_proveedor`) VALUES
(1, 'COMPRASHY', 'HY HAO YUN SOCIEDAD ANONIMA', '80113215-0', '981531531', 'Ciudad del Este'),
(5, 'VISAO VIP', 'VISAO VIP S.R.L.', '80058606-9', '212376544', 'Shopping Lai Lai Center - 4to Piso y 5to Piso - Ciudad del Este'),
(6, 'ATACADO GAMES', ' SAFI ATACADO SRL', '80064388-7', '0615 11053', 'Shopping Jebai Center 3º Piso');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_ram`
--

CREATE TABLE `pagina_ram` (
  `id_ram` int(11) NOT NULL,
  `cod_ram` int(11) DEFAULT NULL,
  `marca_ram` varchar(30) COLLATE latin1_spanish_ci NOT NULL,
  `descripcion_ram` varchar(200) COLLATE latin1_spanish_ci NOT NULL,
  `precio_compra_ram` int(11) NOT NULL,
  `precio_venta_ram` int(11) NOT NULL,
  `stock_ram` int(11) NOT NULL,
  `imagen_ram` varchar(100) COLLATE latin1_spanish_ci DEFAULT NULL,
  `nombre_proveedor_id` int(11) DEFAULT NULL,
  `tipo_ram_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_ram`
--

INSERT INTO `pagina_ram` (`id_ram`, `cod_ram`, `marca_ram`, `descripcion_ram`, `precio_compra_ram`, `precio_venta_ram`, `stock_ram`, `imagen_ram`, `nombre_proveedor_id`, `tipo_ram_id`) VALUES
(1, 819916, 'HyperX', 'RAM HyperX Fury RGB / 16GB / DDR4 / 3466MHz - (HX434C17FB4A/16)', 550000, 630000, 4, 'ram/Hyper02_hkc8h4.jpg', 6, 4),
(2, 302043, 'Hyper-X', 'RAM Hyper-X Fury black 4GB / DDR3 / 1866MHz - (HX318C10FB/4)', 240000, 320000, 6, 'ram/memoria-hyper-x-fury-4gb-1866mhz-ddr3-atacado-games-paraguay-paraguai-py-302043-1.jpg', 6, 3),
(3, 31060, 'Kingston', 'RAM Kingston Fury Beast DDR5 16GB 4800MHz', 1325000, 1720000, 2, 'ram/537612.png', 5, 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_reparacion`
--

CREATE TABLE `pagina_reparacion` (
  `codigo_rep` int(11) NOT NULL,
  `equipo_rep` int(11) DEFAULT NULL,
  `desc_equipo_rep` varchar(200) COLLATE latin1_spanish_ci NOT NULL,
  `horas_rep` int(11) DEFAULT NULL,
  `actividades_rep` varchar(200) COLLATE latin1_spanish_ci NOT NULL,
  `inicio_rep` date NOT NULL,
  `fin_rep` date NOT NULL,
  `estado_rep` int(11) DEFAULT NULL,
  `nombre_cliente_id` int(11) DEFAULT NULL,
  `nombre_completo_usuario_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_reparacion`
--

INSERT INTO `pagina_reparacion` (`codigo_rep`, `equipo_rep`, `desc_equipo_rep`, `horas_rep`, `actividades_rep`, `inicio_rep`, `fin_rep`, `estado_rep`, `nombre_cliente_id`, `nombre_completo_usuario_id`) VALUES
(1, 2, 'xd', 1, 'Cambio de pasta', '2022-01-01', '2022-01-02', 3, 13, 16);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_repuestos`
--

CREATE TABLE `pagina_repuestos` (
  `id_repuesto` int(11) NOT NULL,
  `cod_repuesto` int(11) DEFAULT NULL,
  `tipo_repuesto` int(11) DEFAULT NULL,
  `marca_repuesto` varchar(30) COLLATE latin1_spanish_ci NOT NULL,
  `descripcion_repuesto` varchar(200) COLLATE latin1_spanish_ci NOT NULL,
  `precio_compra_repuesto` int(11) NOT NULL,
  `precio_venta_repuesto` int(11) NOT NULL,
  `stock_repuesto` int(11) NOT NULL,
  `imagen_repuesto` varchar(100) COLLATE latin1_spanish_ci DEFAULT NULL,
  `nombre_proveedor_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_repuestos`
--

INSERT INTO `pagina_repuestos` (`id_repuesto`, `cod_repuesto`, `tipo_repuesto`, `marca_repuesto`, `descripcion_repuesto`, `precio_compra_repuesto`, `precio_venta_repuesto`, `stock_repuesto`, `imagen_repuesto`, `nombre_proveedor_id`) VALUES
(1, 9872, 2, 'HP', 'Notebook HP 65w Azul', 177500, 216463, 3, 'repuestos/fuente-nb-hp-65w-azul.png', 6),
(2, 30866, 1, 'ACER', 'NB ACER AS09A41/AS09A51/AS09A61/AS09A71', 270000, 329268, 1, 'repuestos/bat-nb-acer-as09a41-as09a51-as09a61-as09a71.jpg', 6),
(3, 27556, 2, 'Power', 'Ley-27 120W / 110-220V - Negro - Universal p/ NB ', 96525, 117713, 2, 'repuestos/528140', 5);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_tipo_cpu`
--

CREATE TABLE `pagina_tipo_cpu` (
  `id_tipo_cpu` int(11) NOT NULL,
  `desc_tipo_cpu` varchar(20) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_tipo_cpu`
--

INSERT INTO `pagina_tipo_cpu` (`id_tipo_cpu`, `desc_tipo_cpu`) VALUES
(1, 'LGA1151'),
(2, 'LGA1700'),
(3, 'sWRX8');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_tipo_gabinete`
--

CREATE TABLE `pagina_tipo_gabinete` (
  `id_tipo_gabinete` int(11) NOT NULL,
  `desc_tipo_gabinete` varchar(20) COLLATE latin1_spanish_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_tipo_gabinete`
--

INSERT INTO `pagina_tipo_gabinete` (`id_tipo_gabinete`, `desc_tipo_gabinete`) VALUES
(1, 'ATX'),
(2, 'ITX');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_tipo_ram`
--

CREATE TABLE `pagina_tipo_ram` (
  `id_tipo_ram` int(11) NOT NULL,
  `desc_tipo_ram` varchar(20) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_tipo_ram`
--

INSERT INTO `pagina_tipo_ram` (`id_tipo_ram`, `desc_tipo_ram`) VALUES
(1, 'DDR1'),
(2, 'DDR2'),
(3, 'DDR3'),
(4, 'DDR4'),
(5, 'DDR5');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pagina_usuario`
--

CREATE TABLE `pagina_usuario` (
  `id_usuario` int(11) NOT NULL,
  `nombre_usuario` varchar(10) COLLATE latin1_spanish_ci NOT NULL,
  `password_usuario` varchar(10) COLLATE latin1_spanish_ci NOT NULL,
  `nombre_completo_usuario` varchar(200) COLLATE latin1_spanish_ci NOT NULL,
  `tipo_usuario` int(11) DEFAULT NULL,
  `ci_usuario` varchar(20) COLLATE latin1_spanish_ci NOT NULL,
  `telefono_usuario` varchar(30) COLLATE latin1_spanish_ci NOT NULL,
  `direccion_usuario` varchar(200) COLLATE latin1_spanish_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_spanish_ci;

--
-- Volcado de datos para la tabla `pagina_usuario`
--

INSERT INTO `pagina_usuario` (`id_usuario`, `nombre_usuario`, `password_usuario`, `nombre_completo_usuario`, `tipo_usuario`, `ci_usuario`, `telefono_usuario`, `direccion_usuario`) VALUES
(10, 'ALEX', '12345', 'Alex Diesel', 2, '1', '1', 'Obligado'),
(12, 'JUAN', '12345', 'Juan Kiernyezny', 1, '5195110-0', '981116134', 'Encarnacion'),
(16, 'ANDRES', '12345', 'Andres Miciukiewicz', 1, '1', '1', 'Encarnacion'),
(17, 'PABLO', '12345', 'Pablo Benedix', 2, '123', '123', 'Hohenau');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `pagina_ciudad`
--
ALTER TABLE `pagina_ciudad`
  ADD PRIMARY KEY (`codigo_ciudad`),
  ADD KEY `Pagina_ciudad_nombre_departamento__b9e4a91a_fk_Pagina_de` (`nombre_departamento_id`);

--
-- Indices de la tabla `pagina_cliente`
--
ALTER TABLE `pagina_cliente`
  ADD PRIMARY KEY (`codigo_cliente`),
  ADD KEY `Pagina_cliente_descripcion_nacional_049cb96a_fk_Pagina_na` (`descripcion_nacionalidad_id`),
  ADD KEY `Pagina_cliente_nombre_ciudad_id_b40b4d65_fk_Pagina_ci` (`nombre_ciudad_id`),
  ADD KEY `Pagina_cliente_nombre_departamento__dd7b1422_fk_Pagina_de` (`nombre_departamento_id`);

--
-- Indices de la tabla `pagina_cpu`
--
ALTER TABLE `pagina_cpu`
  ADD PRIMARY KEY (`id_cpu`),
  ADD KEY `Pagina_cpu_nombre_proveedor_id_e5b5cf1c_fk_Pagina_pr` (`nombre_proveedor_id`),
  ADD KEY `Pagina_cpu_tipo_cpu_id_f4bed3e6_fk_Pagina_tipo_cpu_id_tipo_cpu` (`tipo_cpu_id`);

--
-- Indices de la tabla `pagina_departamento`
--
ALTER TABLE `pagina_departamento`
  ADD PRIMARY KEY (`codigo_departamento`);

--
-- Indices de la tabla `pagina_gabinete`
--
ALTER TABLE `pagina_gabinete`
  ADD PRIMARY KEY (`id_gab`),
  ADD KEY `Pagina_gabinete_nombre_proveedor_id_b6797219_fk_Pagina_pr` (`nombre_proveedor_id`),
  ADD KEY `Pagina_gabinete_tipo_gabinete_id_4f0eb277_fk_Pagina_ti` (`tipo_gabinete_id`);

--
-- Indices de la tabla `pagina_mantenimiento`
--
ALTER TABLE `pagina_mantenimiento`
  ADD PRIMARY KEY (`codigo_mant`),
  ADD KEY `Pagina_mantenimiento_nombre_cliente_id_671b28bf_fk_Pagina_cl` (`nombre_cliente_id`),
  ADD KEY `Pagina_mantenimiento_nombre_completo_usua_3ec353ea_fk_Pagina_us` (`nombre_completo_usuario_id`);

--
-- Indices de la tabla `pagina_montaje`
--
ALTER TABLE `pagina_montaje`
  ADD PRIMARY KEY (`codigo_montaje`),
  ADD KEY `Pagina_montaje_nombre_cliente_id_a552243c_fk_Pagina_cl` (`nombre_cliente_id`),
  ADD KEY `Pagina_montaje_nombre_completo_usua_9a0ff4d6_fk_Pagina_us` (`nombre_completo_usuario_id`),
  ADD KEY `Pagina_montaje_tipo_cpu_id_2783dfc8_fk_Pagina_cpu_id_cpu` (`tipo_cpu_id`),
  ADD KEY `Pagina_montaje_tipo_gabinete_id_9dccb5b2_fk_Pagina_ga` (`tipo_gabinete_id`),
  ADD KEY `Pagina_montaje_tipo_ram_id_a241bcc5_fk_Pagina_ram_id_ram` (`tipo_ram_id`),
  ADD KEY `Pagina_montaje_id_periferico_id_e931c9cd_fk_Pagina_pe` (`id_periferico_id`),
  ADD KEY `Pagina_montaje_id_placa_base_id_0c5f1f23_fk_Pagina_pl` (`id_placa_base_id`);

--
-- Indices de la tabla `pagina_nacionalidad`
--
ALTER TABLE `pagina_nacionalidad`
  ADD PRIMARY KEY (`codigo_nacionalidad`);

--
-- Indices de la tabla `pagina_perifericos`
--
ALTER TABLE `pagina_perifericos`
  ADD PRIMARY KEY (`id_periferico`),
  ADD KEY `Pagina_perifericos_nombre_proveedor_id_52825213_fk_Pagina_pr` (`nombre_proveedor_id`);

--
-- Indices de la tabla `pagina_placa_base`
--
ALTER TABLE `pagina_placa_base`
  ADD PRIMARY KEY (`id_placa_base`),
  ADD KEY `Pagina_placa_base_nombre_proveedor_id_05d1e60d_fk_Pagina_pr` (`nombre_proveedor_id`),
  ADD KEY `Pagina_placa_base_tipo_cpu_placa_base__373a65d7_fk_Pagina_ti` (`tipo_cpu_placa_base_id`),
  ADD KEY `Pagina_placa_base_tipo_gabinete_placa__6ec161a0_fk_Pagina_ti` (`tipo_gabinete_placa_base_id`),
  ADD KEY `Pagina_placa_base_tipo_ram_placa_base__bde9d3c3_fk_Pagina_ti` (`tipo_ram_placa_base_id`);

--
-- Indices de la tabla `pagina_proveedor`
--
ALTER TABLE `pagina_proveedor`
  ADD PRIMARY KEY (`codigo_proveedor`);

--
-- Indices de la tabla `pagina_ram`
--
ALTER TABLE `pagina_ram`
  ADD PRIMARY KEY (`id_ram`),
  ADD KEY `Pagina_ram_nombre_proveedor_id_8f254629_fk_Pagina_pr` (`nombre_proveedor_id`),
  ADD KEY `Pagina_ram_tipo_ram_id_9eb17a8f_fk_Pagina_tipo_ram_id_tipo_ram` (`tipo_ram_id`);

--
-- Indices de la tabla `pagina_reparacion`
--
ALTER TABLE `pagina_reparacion`
  ADD PRIMARY KEY (`codigo_rep`),
  ADD KEY `Pagina_reparacion_nombre_cliente_id_05984466_fk_Pagina_cl` (`nombre_cliente_id`),
  ADD KEY `Pagina_reparacion_nombre_completo_usua_790ceace_fk_Pagina_us` (`nombre_completo_usuario_id`);

--
-- Indices de la tabla `pagina_repuestos`
--
ALTER TABLE `pagina_repuestos`
  ADD PRIMARY KEY (`id_repuesto`),
  ADD KEY `Pagina_repuestos_nombre_proveedor_id_0b6bbfc5_fk_Pagina_pr` (`nombre_proveedor_id`);

--
-- Indices de la tabla `pagina_tipo_cpu`
--
ALTER TABLE `pagina_tipo_cpu`
  ADD PRIMARY KEY (`id_tipo_cpu`);

--
-- Indices de la tabla `pagina_tipo_gabinete`
--
ALTER TABLE `pagina_tipo_gabinete`
  ADD PRIMARY KEY (`id_tipo_gabinete`);

--
-- Indices de la tabla `pagina_tipo_ram`
--
ALTER TABLE `pagina_tipo_ram`
  ADD PRIMARY KEY (`id_tipo_ram`);

--
-- Indices de la tabla `pagina_usuario`
--
ALTER TABLE `pagina_usuario`
  ADD PRIMARY KEY (`id_usuario`),
  ADD UNIQUE KEY `nombre_usuario` (`nombre_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=97;

--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=25;

--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=38;

--
-- AUTO_INCREMENT de la tabla `pagina_ciudad`
--
ALTER TABLE `pagina_ciudad`
  MODIFY `codigo_ciudad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `pagina_cliente`
--
ALTER TABLE `pagina_cliente`
  MODIFY `codigo_cliente` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT de la tabla `pagina_cpu`
--
ALTER TABLE `pagina_cpu`
  MODIFY `id_cpu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `pagina_departamento`
--
ALTER TABLE `pagina_departamento`
  MODIFY `codigo_departamento` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=19;

--
-- AUTO_INCREMENT de la tabla `pagina_gabinete`
--
ALTER TABLE `pagina_gabinete`
  MODIFY `id_gab` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- AUTO_INCREMENT de la tabla `pagina_mantenimiento`
--
ALTER TABLE `pagina_mantenimiento`
  MODIFY `codigo_mant` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT de la tabla `pagina_montaje`
--
ALTER TABLE `pagina_montaje`
  MODIFY `codigo_montaje` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `pagina_nacionalidad`
--
ALTER TABLE `pagina_nacionalidad`
  MODIFY `codigo_nacionalidad` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `pagina_perifericos`
--
ALTER TABLE `pagina_perifericos`
  MODIFY `id_periferico` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT de la tabla `pagina_placa_base`
--
ALTER TABLE `pagina_placa_base`
  MODIFY `id_placa_base` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT de la tabla `pagina_proveedor`
--
ALTER TABLE `pagina_proveedor`
  MODIFY `codigo_proveedor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT de la tabla `pagina_ram`
--
ALTER TABLE `pagina_ram`
  MODIFY `id_ram` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `pagina_reparacion`
--
ALTER TABLE `pagina_reparacion`
  MODIFY `codigo_rep` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT de la tabla `pagina_repuestos`
--
ALTER TABLE `pagina_repuestos`
  MODIFY `id_repuesto` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `pagina_tipo_cpu`
--
ALTER TABLE `pagina_tipo_cpu`
  MODIFY `id_tipo_cpu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `pagina_tipo_gabinete`
--
ALTER TABLE `pagina_tipo_gabinete`
  MODIFY `id_tipo_gabinete` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT de la tabla `pagina_tipo_ram`
--
ALTER TABLE `pagina_tipo_ram`
  MODIFY `id_tipo_ram` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `pagina_usuario`
--
ALTER TABLE `pagina_usuario`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `pagina_ciudad`
--
ALTER TABLE `pagina_ciudad`
  ADD CONSTRAINT `Pagina_ciudad_nombre_departamento__b9e4a91a_fk_Pagina_de` FOREIGN KEY (`nombre_departamento_id`) REFERENCES `pagina_departamento` (`codigo_departamento`);

--
-- Filtros para la tabla `pagina_cliente`
--
ALTER TABLE `pagina_cliente`
  ADD CONSTRAINT `Pagina_cliente_descripcion_nacional_049cb96a_fk_Pagina_na` FOREIGN KEY (`descripcion_nacionalidad_id`) REFERENCES `pagina_nacionalidad` (`codigo_nacionalidad`),
  ADD CONSTRAINT `Pagina_cliente_nombre_ciudad_id_b40b4d65_fk_Pagina_ci` FOREIGN KEY (`nombre_ciudad_id`) REFERENCES `pagina_ciudad` (`codigo_ciudad`),
  ADD CONSTRAINT `Pagina_cliente_nombre_departamento__dd7b1422_fk_Pagina_de` FOREIGN KEY (`nombre_departamento_id`) REFERENCES `pagina_departamento` (`codigo_departamento`);

--
-- Filtros para la tabla `pagina_cpu`
--
ALTER TABLE `pagina_cpu`
  ADD CONSTRAINT `Pagina_cpu_nombre_proveedor_id_e5b5cf1c_fk_Pagina_pr` FOREIGN KEY (`nombre_proveedor_id`) REFERENCES `pagina_proveedor` (`codigo_proveedor`),
  ADD CONSTRAINT `Pagina_cpu_tipo_cpu_id_f4bed3e6_fk_Pagina_tipo_cpu_id_tipo_cpu` FOREIGN KEY (`tipo_cpu_id`) REFERENCES `pagina_tipo_cpu` (`id_tipo_cpu`);

--
-- Filtros para la tabla `pagina_gabinete`
--
ALTER TABLE `pagina_gabinete`
  ADD CONSTRAINT `Pagina_gabinete_nombre_proveedor_id_b6797219_fk_Pagina_pr` FOREIGN KEY (`nombre_proveedor_id`) REFERENCES `pagina_proveedor` (`codigo_proveedor`),
  ADD CONSTRAINT `Pagina_gabinete_tipo_gabinete_id_4f0eb277_fk_Pagina_ti` FOREIGN KEY (`tipo_gabinete_id`) REFERENCES `pagina_tipo_gabinete` (`id_tipo_gabinete`);

--
-- Filtros para la tabla `pagina_mantenimiento`
--
ALTER TABLE `pagina_mantenimiento`
  ADD CONSTRAINT `Pagina_mantenimiento_nombre_cliente_id_671b28bf_fk_Pagina_cl` FOREIGN KEY (`nombre_cliente_id`) REFERENCES `pagina_cliente` (`codigo_cliente`),
  ADD CONSTRAINT `Pagina_mantenimiento_nombre_completo_usua_3ec353ea_fk_Pagina_us` FOREIGN KEY (`nombre_completo_usuario_id`) REFERENCES `pagina_usuario` (`id_usuario`);

--
-- Filtros para la tabla `pagina_montaje`
--
ALTER TABLE `pagina_montaje`
  ADD CONSTRAINT `Pagina_montaje_id_periferico_id_e931c9cd_fk_Pagina_pe` FOREIGN KEY (`id_periferico_id`) REFERENCES `pagina_perifericos` (`id_periferico`),
  ADD CONSTRAINT `Pagina_montaje_id_placa_base_id_0c5f1f23_fk_Pagina_pl` FOREIGN KEY (`id_placa_base_id`) REFERENCES `pagina_placa_base` (`id_placa_base`),
  ADD CONSTRAINT `Pagina_montaje_nombre_cliente_id_a552243c_fk_Pagina_cl` FOREIGN KEY (`nombre_cliente_id`) REFERENCES `pagina_cliente` (`codigo_cliente`),
  ADD CONSTRAINT `Pagina_montaje_nombre_completo_usua_9a0ff4d6_fk_Pagina_us` FOREIGN KEY (`nombre_completo_usuario_id`) REFERENCES `pagina_usuario` (`id_usuario`),
  ADD CONSTRAINT `Pagina_montaje_tipo_cpu_id_2783dfc8_fk_Pagina_cpu_id_cpu` FOREIGN KEY (`tipo_cpu_id`) REFERENCES `pagina_cpu` (`id_cpu`),
  ADD CONSTRAINT `Pagina_montaje_tipo_gabinete_id_9dccb5b2_fk_Pagina_ga` FOREIGN KEY (`tipo_gabinete_id`) REFERENCES `pagina_gabinete` (`id_gab`),
  ADD CONSTRAINT `Pagina_montaje_tipo_ram_id_a241bcc5_fk_Pagina_ram_id_ram` FOREIGN KEY (`tipo_ram_id`) REFERENCES `pagina_ram` (`id_ram`);

--
-- Filtros para la tabla `pagina_perifericos`
--
ALTER TABLE `pagina_perifericos`
  ADD CONSTRAINT `Pagina_perifericos_nombre_proveedor_id_52825213_fk_Pagina_pr` FOREIGN KEY (`nombre_proveedor_id`) REFERENCES `pagina_proveedor` (`codigo_proveedor`);

--
-- Filtros para la tabla `pagina_placa_base`
--
ALTER TABLE `pagina_placa_base`
  ADD CONSTRAINT `Pagina_placa_base_nombre_proveedor_id_05d1e60d_fk_Pagina_pr` FOREIGN KEY (`nombre_proveedor_id`) REFERENCES `pagina_proveedor` (`codigo_proveedor`),
  ADD CONSTRAINT `Pagina_placa_base_tipo_cpu_placa_base__373a65d7_fk_Pagina_ti` FOREIGN KEY (`tipo_cpu_placa_base_id`) REFERENCES `pagina_tipo_cpu` (`id_tipo_cpu`),
  ADD CONSTRAINT `Pagina_placa_base_tipo_gabinete_placa__6ec161a0_fk_Pagina_ti` FOREIGN KEY (`tipo_gabinete_placa_base_id`) REFERENCES `pagina_tipo_gabinete` (`id_tipo_gabinete`),
  ADD CONSTRAINT `Pagina_placa_base_tipo_ram_placa_base__bde9d3c3_fk_Pagina_ti` FOREIGN KEY (`tipo_ram_placa_base_id`) REFERENCES `pagina_tipo_ram` (`id_tipo_ram`);

--
-- Filtros para la tabla `pagina_ram`
--
ALTER TABLE `pagina_ram`
  ADD CONSTRAINT `Pagina_ram_nombre_proveedor_id_8f254629_fk_Pagina_pr` FOREIGN KEY (`nombre_proveedor_id`) REFERENCES `pagina_proveedor` (`codigo_proveedor`),
  ADD CONSTRAINT `Pagina_ram_tipo_ram_id_9eb17a8f_fk_Pagina_tipo_ram_id_tipo_ram` FOREIGN KEY (`tipo_ram_id`) REFERENCES `pagina_tipo_ram` (`id_tipo_ram`);

--
-- Filtros para la tabla `pagina_reparacion`
--
ALTER TABLE `pagina_reparacion`
  ADD CONSTRAINT `Pagina_reparacion_nombre_cliente_id_05984466_fk_Pagina_cl` FOREIGN KEY (`nombre_cliente_id`) REFERENCES `pagina_cliente` (`codigo_cliente`),
  ADD CONSTRAINT `Pagina_reparacion_nombre_completo_usua_790ceace_fk_Pagina_us` FOREIGN KEY (`nombre_completo_usuario_id`) REFERENCES `pagina_usuario` (`id_usuario`);

--
-- Filtros para la tabla `pagina_repuestos`
--
ALTER TABLE `pagina_repuestos`
  ADD CONSTRAINT `Pagina_repuestos_nombre_proveedor_id_0b6bbfc5_fk_Pagina_pr` FOREIGN KEY (`nombre_proveedor_id`) REFERENCES `pagina_proveedor` (`codigo_proveedor`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
