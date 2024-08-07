PGDMP     $                    {         	   funeraria    15.2    15.2 %    -           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            .           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            /           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            0           1262    16522 	   funeraria    DATABASE        CREATE DATABASE funeraria WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Colombia.1252';
    DROP DATABASE funeraria;
                postgres    false            �            1259    16567    adicionales    TABLE     ;  CREATE TABLE public.adicionales (
    id_adicional integer NOT NULL,
    ciudad text,
    fecha date,
    nombre_comprador text,
    documento_comprador bigint,
    nombre_vendedor text,
    descripciones text[],
    cantidades text[],
    valores_unitarios integer[],
    valor_total integer,
    saldo integer
);
    DROP TABLE public.adicionales;
       public         heap    postgres    false            �            1259    16566    adicionales_id_adicional_seq    SEQUENCE     �   ALTER TABLE public.adicionales ALTER COLUMN id_adicional ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.adicionales_id_adicional_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    223            �            1259    16523    colillas    TABLE     *  CREATE TABLE public.colillas (
    numero_colilla integer NOT NULL,
    valor_mes integer,
    desde_fecha date,
    hasta_fecha date,
    fecha_pago date,
    hora_pago time with time zone,
    usuario text,
    documentos bigint[],
    nombres text[],
    socio integer,
    liquidado boolean
);
    DROP TABLE public.colillas;
       public         heap    postgres    false            �            1259    16542    colillas_numero_colilla_seq    SEQUENCE     �   ALTER TABLE public.colillas ALTER COLUMN numero_colilla ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.colillas_numero_colilla_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    214            �            1259    16576    facturas_adicionales    TABLE     �   CREATE TABLE public.facturas_adicionales (
    id_abono integer NOT NULL,
    documento_comprador integer,
    nombre_comprador text,
    fecha date,
    nombre_vendedor text,
    id_factura integer,
    valor_abonado integer,
    liquidado boolean
);
 (   DROP TABLE public.facturas_adicionales;
       public         heap    postgres    false            �            1259    16575     facturas_adiconales_id_abono_seq    SEQUENCE     �   ALTER TABLE public.facturas_adicionales ALTER COLUMN id_abono ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.facturas_adiconales_id_abono_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    226            �            1259    16543    gastos    TABLE     �   CREATE TABLE public.gastos (
    id_gasto integer NOT NULL,
    gasto text,
    valor integer,
    nombre_usuario text,
    fecha date,
    jefe1 boolean,
    jefe2 boolean,
    funeraria boolean,
    revisado boolean,
    liquidado boolean
);
    DROP TABLE public.gastos;
       public         heap    postgres    false            �            1259    16574    gastos_id_gasto_seq    SEQUENCE     �   ALTER TABLE public.gastos ALTER COLUMN id_gasto ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.gastos_id_gasto_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    218            �            1259    16535    polizas    TABLE     �  CREATE TABLE public.polizas (
    socio integer NOT NULL,
    nombres text[],
    documentos bigint[],
    fechas_nacimiento date[],
    parentesco_titular text[],
    fecha_afiliacion date[],
    mayor_70 boolean[],
    estado boolean,
    fecha_desde date,
    fecha_hasta date,
    valor_mes integer,
    usuario_creacion text,
    usuario_ultimo_pago text,
    fecha_ultimo_pago date
);
    DROP TABLE public.polizas;
       public         heap    postgres    false            �            1259    16549    saldo    TABLE     C  CREATE TABLE public.saldo (
    id_saldo integer NOT NULL,
    socio integer,
    gasto text,
    descripciones text[],
    fecha date,
    valor integer,
    gastos_jefe1 integer,
    gastos_jefe2 integer,
    gastos_funeraria integer,
    jefe1 integer,
    jefe2 integer,
    funeraria integer,
    liquidado boolean
);
    DROP TABLE public.saldo;
       public         heap    postgres    false            �            1259    16548    saldo_id_saldo_seq    SEQUENCE     �   ALTER TABLE public.saldo ALTER COLUMN id_saldo ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.saldo_id_saldo_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    220            �            1259    16530    usuario    TABLE     �   CREATE TABLE public.usuario (
    id_usuario integer NOT NULL,
    contrasena integer,
    nombre text,
    documento text,
    cargo text
);
    DROP TABLE public.usuario;
       public         heap    postgres    false            �            1259    16558    usuario_id_usuario_seq    SEQUENCE     �   ALTER TABLE public.usuario ALTER COLUMN id_usuario ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.usuario_id_usuario_seq
    START WITH 1000
    INCREMENT BY 1
    MINVALUE 1000
    NO MAXVALUE
    CACHE 1
);
            public          postgres    false    215            '          0    16567    adicionales 
   TABLE DATA           �   COPY public.adicionales (id_adicional, ciudad, fecha, nombre_comprador, documento_comprador, nombre_vendedor, descripciones, cantidades, valores_unitarios, valor_total, saldo) FROM stdin;
    public          postgres    false    223   �.                 0    16523    colillas 
   TABLE DATA           �   COPY public.colillas (numero_colilla, valor_mes, desde_fecha, hasta_fecha, fecha_pago, hora_pago, usuario, documentos, nombres, socio, liquidado) FROM stdin;
    public          postgres    false    214   1       *          0    16576    facturas_adicionales 
   TABLE DATA           �   COPY public.facturas_adicionales (id_abono, documento_comprador, nombre_comprador, fecha, nombre_vendedor, id_factura, valor_abonado, liquidado) FROM stdin;
    public          postgres    false    226   5g       "          0    16543    gastos 
   TABLE DATA           }   COPY public.gastos (id_gasto, gasto, valor, nombre_usuario, fecha, jefe1, jefe2, funeraria, revisado, liquidado) FROM stdin;
    public          postgres    false    218   h                  0    16535    polizas 
   TABLE DATA           �   COPY public.polizas (socio, nombres, documentos, fechas_nacimiento, parentesco_titular, fecha_afiliacion, mayor_70, estado, fecha_desde, fecha_hasta, valor_mes, usuario_creacion, usuario_ultimo_pago, fecha_ultimo_pago) FROM stdin;
    public          postgres    false    216   {k       $          0    16549    saldo 
   TABLE DATA           �   COPY public.saldo (id_saldo, socio, gasto, descripciones, fecha, valor, gastos_jefe1, gastos_jefe2, gastos_funeraria, jefe1, jefe2, funeraria, liquidado) FROM stdin;
    public          postgres    false    220   N�                 0    16530    usuario 
   TABLE DATA           S   COPY public.usuario (id_usuario, contrasena, nombre, documento, cargo) FROM stdin;
    public          postgres    false    215   ��       1           0    0    adicionales_id_adicional_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.adicionales_id_adicional_seq', 17, true);
          public          postgres    false    222            2           0    0    colillas_numero_colilla_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.colillas_numero_colilla_seq', 255, true);
          public          postgres    false    217            3           0    0     facturas_adiconales_id_abono_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public.facturas_adiconales_id_abono_seq', 10, true);
          public          postgres    false    225            4           0    0    gastos_id_gasto_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.gastos_id_gasto_seq', 86, true);
          public          postgres    false    224            5           0    0    saldo_id_saldo_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.saldo_id_saldo_seq', 319, true);
          public          postgres    false    219            6           0    0    usuario_id_usuario_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.usuario_id_usuario_seq', 1008, true);
          public          postgres    false    221            �           2606    16573    adicionales adicionales_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.adicionales
    ADD CONSTRAINT adicionales_pkey PRIMARY KEY (id_adicional);
 F   ALTER TABLE ONLY public.adicionales DROP CONSTRAINT adicionales_pkey;
       public            postgres    false    223            �           2606    16527    colillas colillas_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.colillas
    ADD CONSTRAINT colillas_pkey PRIMARY KEY (numero_colilla);
 @   ALTER TABLE ONLY public.colillas DROP CONSTRAINT colillas_pkey;
       public            postgres    false    214            �           2606    16582 -   facturas_adicionales facturas_adiconales_pkey 
   CONSTRAINT     q   ALTER TABLE ONLY public.facturas_adicionales
    ADD CONSTRAINT facturas_adiconales_pkey PRIMARY KEY (id_abono);
 W   ALTER TABLE ONLY public.facturas_adicionales DROP CONSTRAINT facturas_adiconales_pkey;
       public            postgres    false    226            �           2606    16557    gastos gastos_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.gastos
    ADD CONSTRAINT gastos_pkey PRIMARY KEY (id_gasto);
 <   ALTER TABLE ONLY public.gastos DROP CONSTRAINT gastos_pkey;
       public            postgres    false    218            �           2606    16541    polizas polizas_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.polizas
    ADD CONSTRAINT polizas_pkey PRIMARY KEY (socio);
 >   ALTER TABLE ONLY public.polizas DROP CONSTRAINT polizas_pkey;
       public            postgres    false    216            �           2606    16553    saldo saldo_pkey 
   CONSTRAINT     T   ALTER TABLE ONLY public.saldo
    ADD CONSTRAINT saldo_pkey PRIMARY KEY (id_saldo);
 :   ALTER TABLE ONLY public.saldo DROP CONSTRAINT saldo_pkey;
       public            postgres    false    220            �           2606    16565    usuario usuario_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.usuario
    ADD CONSTRAINT usuario_pkey PRIMARY KEY (id_usuario);
 >   ALTER TABLE ONLY public.usuario DROP CONSTRAINT usuario_pkey;
       public            postgres    false    215            '   h  x��SK��0]S�f��>�,��@�]7N,;�66�O�!��z����1fݘ)�zz$�,�u�AI��2?*��� ���g;������O�*S4�B��� S��h��� ������]�GKhک�0V�N|�vdb�F? ���*9a���O��>��@4���^AK�~�����݅�3c,�Ն�J�WcB�B���;JnK���ő���w������4������	ZgF+Ce�
���)��\�÷]U)��ػi�yٶ��;=�Ȩ���i�(
h9�6b�:қy�M�:�v���a(������@D�zQAh�Ѝ�^J=ƞ۔�o�d4UT��Jmw�(�O�C�3��S�	x��C���z�֒���dwH����Q�&IF͖cE�P�v���?�Od{�KӒ�xi�O��¢!2Y�j[�rP���g���z������nש櫒a�Ȳa�F�T�(Pç���
���&��Nh$_�w���p��;L����[�����?��%���c�z�&�j楥���)�mӅ.U�D��429�94{u�����D�����RVr��(�7J%i��R�Y�N3�QJ�R���{�N8�Ha����A���a(            x��}Yv����3��<z��Ą!�2�$�df9�I�<~I�h�6Ut�Xj�}��)�o�� J^@[RD7���Z7'�)�N�2�[��5�\��R�mgʞ��[U�\y~zY|8�r�|��_�_mm{��?h��4<Y��Vi���sՙ��ǫTmh<?O���t�J�;���:��.U}�,\6�[��2�V����N~>�>�p<�w��P��O��W�����G���H:���?mtk��ԧZYYWJ�%���ֺ�K��	7mൾ�>�>?��`�'�����v�����^>-��O??.����Ac����㧏�/�-��A���wڏ�v�������������?�~~z��Ոo���)��ϥ�t��gƟ)�O�ѭk��9j<�F�l��9R��B��8�@����&�;�����G����Oo0��/�O/��4�����O0o/��O�6�Tx����c���#�������O������w���Ooxoh�'q���{\�|~\�^~�K���<ͨ�K{f<��ʌ{��O�̴�ܘ�L�j&��Ϫ)�l�h/��᥮�n��uS�\����	<>~�����|~y��w�������`��t\\?��~�=~|�I�>}}�'>K'4��49>��R���z���?�0���������z����f�:q����l�&0��1.�v|��K�z�t�6������#����
�y��
T��qq,��������y��O?.�5�~��q��O��ρP�7��>~]|w|���������!�P��>��T6�:;��ʜi;3Cmmjˬݛڹ��ڶ	b�����x>~����<�����;��/���/O��8DA+=ӷ�����x|��5o��o]%Ҩ�_[�$-��E��u
�Q��6����y�ϟ��w9����z���R���8��_��O�O�����4�^�|z}RYt�����[���'�!�����b���g��e��zm@=���2��Ϗ��֑\��v�/�@ho�g_������r����+�5{�^��*(ɤ�3��5g�9�n��j�5|������^x���}Y���==�2�_?~��yw���^�^~����p�^��m`Չn�����W��GF9l"RW#a 6��S�
�.u��BH����]��永x��9���x|{z���_�b�����if�I[��`L��3.�x����_�_^����N��J�B�vF"-�Gsa�_=���)��x�f��ю6I�=H�ǯ�U_9����;X�������q����n�>|aA����/ld�KU��񅝟C۸b���=[��H���4 	E� AZXT��n������Z@�(�7�ϟ_>e���ϰ�h}�ח�𒱳�V+�)���?`�m��||~��#�3π'X�~$�����?�,֏���30Q04Q��rX�6Qy;Z�������+���G�^9�m�if@h^s� @����o�K�$���$������#I�Q{������\q�����a�/��P\����'\�;i��P���u'V�[^��T1�Ҁ�&��N�c�, �h�^��%�8k��4(Gu�P%���SK�ۿ bB���$�ZZi����q�/�?>F��uD=(� +��`4�Ф�	����H��:�'�)��]�_�^
���A���L����ͦy��)�s��5O0L``�5�uT+�6���+�:��CTJ]x�c�x+���R�����8���#�0iX�@w�&o?�u2M\�価2p����:��o��!6���^ � ��׿���}���1lҝF�p���a�>�����QCN�Z�i5�MC4�cf丆�8��)Xڟ��M��i� i�����T�x�M�[u��[\t���v���!0�Y���⏇as�C�@]���پ?kt��ݰ��͢[��8�6�v�/���v�����au�ש���?�{u��7���!i�c
�0���LV��|����N�פr��}�������E��z���aSp�Xmo�����_\o�����u���;�o��V�	o�K�W(H�Jh�/1�{��	�i*'����P��*��ب�ư���H�`>��`�Z��l.jU�%�	���������K^��p�]����a�Yl&�\:\�Ų��Y�"�g��o7��-�]��绖���~�[Hs�C$ws���ly�>t�x�_w9%��~q	���ϛ�H���{�6y���|��m��a�[b��n�;���a߸෷��~�vك��&l3�O�6������<!��w��=ܝ};K\f@~?t�:ڌ�͚9�Kd��	�vSKo p��ܽ�D8�E];!��+���bX��7��xɶ@9��1���������jԷ�]ɼf��#Cu��0�&��T�/�4jn6@>N�H�]ck�0�0�phM`� �,�U�Nq�lx���n�!q�ϻ������v���6���p��n���f���'��q�>t��¨���]8*P�I�b�_lG�����sE�r�ҷ;uVMU���6�4�C,�K�X���r���D��ݮ��.x9��ˍM�ѣ���\�Ѩ���l�=,͂�M��4�CLC��r��-�2���Ix��gf�Y�l�X[pͨ�����a=��r��Q5��e�;�%nA�L:��([�e�;�K`�1�ؤ	r;;r��c����C�#���J4K�y��Z�	�vkL�Ko��+���p��7�,N�,� �{ 
k�)@1pK@ �Fn e�>ɟY�ġ9ꊎ~9 ��Αi�=���z]�n5l����Q�IfN�؝+�ӻ�s�М��L����#f���6 ��]�O�i���
���>�o��ڕa��*T7d6�0�yI�(�`��m�<��f����Q�0��Ѹ���L2]Хn���i���.6�d4��X�Wj�Ѭ��v��F� �᧭cJՍ��dI��ӆ��A�~(�&h�#���mχ�����րkA� ��h�{`��ݮ��� B9����[���8u��a� B�J�*O2O�i+�=�q�|J���r?_pΐ)o�%��ԇ���nu��w\Ȟ}��Om�
��s�dޑ!  =c]]{M��B��6�*Z���2�b^��m.�Gd����p�#�9�?Ƅ�n�u��~�/~��`K����Y1�nG��2��=y�Ak�f�ve�L��G��e[_�2#����w��݇�6�g��$B� ֊�
Y���W���ȝ�'��1Ǥ��+W��u������	P���"5�{
�5��:�?�����?q^�*5~&a4�{��ς&�����= �S�fHoU z�-t��-p k���3}V�E�ԘS�<��^�̺y�%~;������htP3	�Uz�+���-}zEr��|"���E��U�.[�5�Ѳ�Q���t�,��ח;�'IQ��"l��@�g��
�Ҁ��b(6�z8��h�Vl$ YVi@6}?^��/Q@��2�x�=Zk��2��R��j�BʪJ	���e�8�M ���m�{+ĸ�����lI�_�P�z�{�"K�u�n�*�vvXP@-��:�d<������Do����(Cj��W��tf��vC��������d�����5*��S�=Aݰ�q�	ㅯB��{���a�)y�,�sj�{'L~�Q�pf�q�Ap�I՝���D�:��Ӟ���:Y�����]nȈ���{P�w$K*7֥�f.�%�(̞�_�8�*�&� P�;�(��V�<Z�<{�=�h�OeZ�9:�Dvۡ�m{�oӼ^�:��}$?�q��6��f���h��� ����&	��7ز�� �E�+�RW��w����[MD�A�ͫ��bЩ��
�v}*~1-qʷ�R� x+�.ʓqN�߆(�v����]�����C��Vظ0�M~Lb��'��ԙ�Eр��`ۈY,�~w�;^'>������;D̍�Qv����'bN)�۠��f�\ٕ:    ��u��aׯ�d��V�%b&b��ˁ�  �!E	t��m�3��d�����l���.1���a�&d��=ߌ�}���KT?a�4�U�~��o�
�S5hB���5����%�a�`��ԑ~/^U�i޾X�wF[ �B֎PsGjz�.��Ԅ!���"d��4/�L]�dXؠ��W��`365L�)����mr�z���Ɋ=��b���SAEbr/-�JxJb/��M�gn�m[�hP�i�*`"�n�j��V�*���2���v���dvϸ!k	Vw�������/�4�S��q�9�:�0��xZ��-�.U;�� �#-��gnj�e��5�Q�w��01��P,@q�w���[�o T|\��~���&��~���p7�	�9]=1͎C����%~����u,N;�I���&V�H.��B�pA��ˀo��ڌ�R_�b���v�,vd��Ho
���TS)�gH��m����cL�h ���kT��D]����rɿz ��ZMzW���E����`b�>����_M�Ȱ�S����)� -A�ƙS��L��H׌i��x�vU���eU銂h��xm�
;��n{1D?�6�r�Du���l�M���HA8A1�')������i��5�Hiu�Qդ��e��A���)�s�!bٵ�����p����&�,e���v�.Ǜ�����53���p����n�7��;6{�'�~&����0�qơ�����4�F��Q�n��	2��Ȋ�X�.�� �Ң���?b���]rܠ�V~X�7iؠ�I�2x8@�'���߄�����6b���v��D9����������i?��%:֯��,�7)����Ʊ��Bh�R���\��  �[�!>!G���wŇn�];����A����OT\�&-�.�U�s���p�:��R4VW���������
�SY{����~B�353�� `��3W�˫S������jy���j�s�x7��R�Da� ך�ק��F`_b �1�aSJ�a��pؐ��qt��v�������7�_|ס��i�[�W��8��b��M��-Fd��홙��G�jq�{r�=�F'I��: ��p�\�ZQOF�v���'���c��d�u��"]��#�i�S�.�Z-��Y�3 ��a�[�Qzu]�·���6�q8��6��,�伿E%�P��1�he�#o	#���<�j��R�c�ifs��nP�����g��LG�b����XTx&6�;�7�U%�jh�V���8�V"v &x��y1F:%�ɪ�5����ߖM
�
�Ek -����6�V��k�Jf��
��е�x�y�R�������q�;��w�B)��Wh�[/�G3�\��ѐ��$�s�L���nb�g�,WK�����G�A1�%�u��[A#���D�����uȃRڅ��'��e�b*ɹ����sȓ���b�s3�s�?=����A�=�?1R1��'�}RZY�i\��eNT��������F��sU�mM��P�p�+�A��F!��1���uE��#_Om�$(���`8JU+����(��	�&�9��6�|� r_o;���)
'k�I�Z�gv~l��
GƲGUԝ�d��(��:���]�M�p~�W��e��n����u��kjZ�qD�J��Gr�dϬ>�s9��4��4rլ%�rO.�.�6���n���|/0�}�PoᏰ�?�;�	�$�M�/��TO�_$�L�� |Śf�+l��HC�p�&�
(�׺��֮&ِ)�+͏p/ޣɸ�9��p4���ǽ7�H3qF4TpXr/a��+`$��Qn$c��{������튄B��ٛ��|ɳ����3�c[[�d�b�d�Z���n�![1�����{ȢHػa�La)����f.��ނ&�8�����S�t$�݂8y�*`��E\Q������',d�~3��n�7|���t�O5��?�����'�s�r�bB�oHB����ph��K��`�X��ȢTs�0}�n0A=fX@��0g�usZ�9�J\Xe��q�W��J�
�C������:��U���+���n`����[`�}���r�V�۾���q��������#������Gs�b�<)�0M7�ёU��bcӫ#�QM�rmK>�vT���u�b�u} @��n�m��/|
�eۜ0�7d��I9�4�J�1y������m��|,��#;t��l��PY��V�Q3����]�0�.f$
�Ԙ���� 0��a3$iR��{��	/�z.Y���n
�Θ���n��m�
���/Q�3p��\Mݚpv�D�Ӂ����E���	�q�/P�/#��Y���E��R�٘��`��yz��i�He2X�ф � K0����ږP��"���;� LA�5�9�(@��H~�2�x����6���<i,uwl1�۷l%��G�ZU��������ٓ�6R��gw�bK
;�/{����Wr�uR���3��4��5�Z��a�-~f���MVR�[���r�V��ģ�i�30T��yckۭ�^�R~c�YCf|�&33��ju�%��9�r�q�{/�G�y\�	2V�Z%HYf�;$��gٽ�����xf�ls�򮌂f��3oA�&�<NVU�WM��H��K椤j:�� �U4�԰�Sd�S\��Ԁ�8$�q�S�D���.�IWs�9��e��-�F��k�q�����R�)���|�M�I��C��Q M�H���>z/�#�^"vRX�z��r410ڒD6>2��$��k	�s7��/f;D}�ױ��^� Y�J~�b��)Op��Edu�X1��l������Y@TH��c����d�Qo�X�逈(Μ�2-�q�˩q�,�<9\�d��s\��p��靑H�
�|	[DJ�8�UR��I���@��d�z3��Hl�lಋ3$ٗ==��Q�I�籸3cqT[&`���C���)��Q��q��U�䌣K���!}�Ѡ���O_��02�k+�_u�B�� �>�{$�1�&4L�3�D7A����*���c3yFX-�q�vr4��"��@�f<y�[�*�'�#lo�d�Ƞ�C��o��6m��P�C�V(	�S2P�cRf7��$)���7��٘3D(R��&�M������q�<�t�4�65������֏�	RX2]�q���J��38������SP�)�����16U��X��``������"�H !�,i&D)���{�-��bu���DY"E��r{0;I�KMY���*��s�gP��FK((�u���
T����+UdG��aNa&o�@�,$X���&��\n؄�������	�j�`�����>��7�4g���uQu�՛��"y�$��j�#H'j�yg����a����JHA��������@���Kb�'ޓ�ΛQ��1d�:�Ygz��@
��j�j\r4HE�q��!��-�
>=[t�"gy;V�GՉ[RRK�~.���"�n V���؄�U���u���<��<�7�`��D�ݐL�� �0�ow�� ��W8v!JC�z�-�;��<�]w;rS�-H@�Xl[tU�b{<@f��Tc*A1u�B����iA�� r,�D����)Z���Ar��z��N�M(��YLU�f�3c�~}9����M,g��Α��Bp�h�Is��ŕ��8~6�H�胂�u: �G���M(��~���j\@7Wȉ�u�@��jj�!q�~Ķ�I����@ e6��^M���&��z��]��ԯgG��Rmlb��z&�J9����$��pP*�d�ٜ0�a#�_N|�M,��y�h����^�����_l�������]ˁt�d"��=0��dz+�9B>cK�JR�/+����ߒ�C�2�C�s̃���Ik1���
�l�d��[��T��V�P�ζ������"�S	fIH�=!�*ڜO��b�?�@q�@)QW����Z.v(�&f�w��m�,�&����bL�c�-�%��&��HY��|gГg:Q���Q|���    $}�:��5&U���X4XW�(����� �zp*�N��R%'OQ���*,��[���[�C4�<���nw�k��A>�%N�%�	*�缚����L�E���L�8XG~��?�FV�U���4��'�ܦY6j.����+,���Q��&�C�����rn�1u�17��53�]
�`o���ɏ���*���Q],���G���s��?2%�2��F���Y�Έ`S��@��2&�18��S��Dմ��jZ�z��[q��lit��<lH"�Iu�(��R!6�w�h�;p!za ���ҹ�Ր��J)�}�)�A���A��3��:g40���N�;�H�� ~�F��
�F7n��Z4E$�?� ݊Ս�0p(v4\�C��_���!,��
\�Jn�B���ղ��$�X�5�맖҄��G���l ���߄�/�k���8����d|	�iREMx]����a�ݲ�b�A
Z�i;�f�������J1��<�	T��i���9�՜�$&��S�1>� 6���!x7cĕ�%�Y��	٨�NZ�%j�u��Q>htB��|��n\."�%�9�ׄ|4}�;�N�4���:kRX$ls`�q�G�=�C4X2�ct������7�+�P�S�f+ҋF}�C��k�"��5�R5�	��,r�+�`��y�̸������$&��8]�-M�BI��ݻ�)q*�s!�kN���2rHx�2*�R�����Z_�r��fd�Vu�!��5B�)򎪀u�� ^�3^i� i]'�H�e@�`��-�)�<�FzI�U@��nVc3�~��w�Kue�C3�!����IJM��5,\HUV�x-*���}S�#A{���u�˾Th��ct�pkq^d�| N_i��U)�9#�Z�&��ǰ�<d�>��<n�����;mP��)k5)}P�5�O)���T��./�rhj8杜m�>��$�ɟ���27 �� ����N��Jbaov-�?*�<10R��O�h�O����X�Y��C���S ��:��"�?cG�6�@"S�{�v��h��
P,���cQp�y�
&�x����ݤh��3��R�C��l0�8�ƒ\������=��|�E�v9��c���с!��rfPyW!��Q���8 ��f��
�e�)�&`� �ˡl����M�.�GS���G:�dut(�δ~wu�����Н�bJ�}��QKAdW26M�"����z#<�6F��4�x����[��L���9�`�'�氿��E��f�Z���șr�IS5���2[&�6�r��=Ai�
�,�$�1- ;
�}Y��PB"0��`3���<w�݆��x@�r�졦:G�#D *�;95�Kk�UH�qF��9���j0X}�H ������<�,���,� W4%��Y}G�*&H��0G����[�+�l�QJ�?���@���dZ�-��}�<WFD�(�И�3h�I���'����zu�k��zB�H�g�Ā��z_�;�𪵳���F��Di�.%�B�v��T�%;�7�R�Y�xTx��I�.�	7�\��X��1	1͒k�_f��jx�!�ɵ �/n�,^1� �{+n� U�oKX��W�E^����O�1q�.�Vrd�Ԛho��2g�%���g@�%;���شI������;0[ի��F�� �b���|y۷�\�\�C5��*2|"�߇��,�pTs��B�r� Z�a��4����@�;9�ҝE����J1�Կ)�|�v�z�XK0��
��鴡XT<�6b;�Z�Θ��a-L3����⠹��vw)�BQک����o�Jݼ?g�$��Y�d=��H�`�*{R���k�q ��+��N�f�v
���o���Cۖ�)�Q4�♼��� r��+���2�,�6.*vޥ��b�d�\*Q��9D6f�R�3��p�h4�y�����d�Y�i'�c���8��H��H7Q�p.]�|�&<߁���o�뉷�*�
�N��钼o�2XC���&L�1!�0h�Y}���\�Ek*1M4ڎ*+2$L����������HWz3����^cg�yQ���t�y�=�p�:�êH�%^�d1��C�yV*& �<|���\���2S灎t8_�D������^b����q4��%Ae�C����LQz�Fv؎��D7j��d�W-����G�x�*k< 8r�^���Z4����1|u@��ΰ:�r���s���j�(
��-5`�.�+y5$C�JCL��h)�LK(�\�t�`e�)ta8�45&�913��T&}�0���/L`sj1�3��$�e�dRI��\�b` �7��ɠ#��f�QD�O|G�/�=R:՘��H���:K<x%=Q�����&l�#��ڝ��7�g�|BES���,4�������q��5��%\a4�_e��l��-;F���L�YPC��.��*g�$)�U���T��/�'�ȩO��jG���)�Si�V�'m4mQ�S�SZ�h�]ɂ�^�=F��M��Ԯ����RR�G��OBC3�U�Ɋfܨ�Y�͡8����k<�����c�z�QEEdf���1eX���$��
�S	�,�}��r�|DC ̀�Q�֊a�j-a��w�c<r{
x�^O W��$~Qc�>��j��Ԕ1k<�?�����Y�r����|p���EZP ����n���ۈ�3�j�=ʽ����oo����8yA1�����+��zt��8���)��`"�l��B��1���7.T��Lri��F%����7VK��Þ�d zw
m3�L��%5r��z.���;`v���Nc����=��Rݡ���u�>!Æ��@I�)���`(��_<�����w�Uw�w@>�t��LB��0����eJ������81X}b>:�91�y@7��`�żKՆ�6R莳�rK:���M�r�R�����������	�K��,#���5����3���U�b�i� ���#L]UMʫ��j��x�E#TR��Hr�D����i[����{ �[!�n٭�М�$�<�K���Wn�^*@σ�l���R�id���C��3Z�*N�7��2I��z�(�-��;�Nl9��^�w˒7�bYrVU��a"��9��'6"�%�[��W��i>�`lĶTȞ�K�����l.��v����걂DXS�2G��d?L�jU�'�A�N:�(�p3��s�'k�T��˖i��q�2��.��",
X�s��9Ί�	�;��e��ބ)�)(�C���[��&b��"�@����&�3�i��H�I�0�qs�і]T���5�x������f���h1^f��T�%H\T@������PY�Np�7�aD,Fzn��Be���әqYO�P�5��Y&��C΍��謉EMɒ-������x� -ګI��>��"��>'+v3s*�X���Ӎ+QU>�)j�2��|4�&�Q�Y�����!`��#����@7l��������7)����.F�$���7��lJ]�n�	d���˂*vq�V�RP�3�v:	�R��\u��2���ѭI]%ڬ�0K��'������q̹�lEO#W6T�-fx����F���G�KVC�CO2��nʲ�=�y9�*o��Y̐��J���������`^�#.
��}~�fs/�
�yT�d�#�VL:�$(���j|��X5���)��}�$��X�bl�uuK�N���uX�	��U- �`;&.�&���x��kK(=L�>���>b����GS��Y���^Y�-��O�S!��jה�p v=0�z9\�� ��cr�X�b�2Z2�xè?� �2��Q��n�q�0��D*Ck���$tP$�ه`|��� ���2ڸ(�.e�"?�;��ט}H�Cm�m���۩Y4Ƣ�fe|
��5Eg��)�M���P�5�R�J]�	�ԡ��
J��COŮH(�rtN�}�!�&:�]��~Y�͂J�JZ���R�4���<������_��7-�6��v|�T��B��㑍�����=����R�m����ԕ   ���i�������z�%$D"&0�@����a���3X����ioO;CY�p���),��؏��S��Ґ����~OϵZ

��47��=ƭ�E"��a��2zy�(���b6d�t�ĕ��#��J,e�T] :��׶1Uȸ&�Ǯ����ޅ�y*S���7�����Z
M4tu�k�C�cLa����	1py�����3/�_�U�����6���#jC/'��:x 1 ,�!>>7��lҋ���AiA�
�$���Iz����ƅ��,"Ũ�~�t���\n�P�,t��6T7V���z@�%qV$����}�& E	��R�!��w�!!�Y��mj���\���(/V���ξ�ء"v9+�Ƚ�
�-�t��r�x�u�۲�u���E-S|V9�b��C�ɞ*�}��z���a_ƙ��rl�G���Y��3̿r��FD,&
J�q<w�?�~z���8��r���������b�����?�|:.V���ǯ�O٭���z���4�D�t ��nB��T Vn��7i0M�R��U%C�Ȣٲ�\��$d�$�9��ڲD��jM��@��v�ҿek��M�����PK%(��N���)�P�mq�ӱ��]�0��@I4e�
����dA���ҺQ���T�*��*HQ9�j{�U|�@6	���ef)f$������iR��Ŝ��\J����G�u��Ӹ�G:%����><l��L��!�1-�1�����v��1>�s�MD����~�u)<�"��R���<+�K��6+z'>W("�����XꖂO�Ԩɗ"K�YZ��-W!K8^����P� Q<�O���
O9�`k61����V�&i�*Vni�d��V8 �> ��(E[��&G�
Z��y.,Rv&m*�=#����TG^B6�!C���3l.1�m#�LǙ��22FP��{UU(�<���3e�������󌢙��{Pз�Q1���K��\f�:NA���U��	_ҾoVA"rU,�c���9v��7���X�Ӆ���֮Śd��y{%��Y�;౬2P�2�?Q�84ۥ�5�o�=�7Q�W���աXUhG����:r�&i��
x��k�:!VS�E	 0h�4�伭���N��0�$�l/�R'gz�%�����}v��J���Z���&�����@�X�&U]�2�**9�*|TjCQ$��/I��+*��HWu����";�l���hH`�}�:<���q��`Mu�t�/�}~nw]���P�0?;X��_*0Ф���Nz�����-4�<��4��F�sYɝ��.S���
���Sԗ�$�ڃS��+3r�N|�&D�iţ;�X
l��Y���q��T$��������1fh#F�=����$r��ݴ���"\eGPc\l����(>�>�p<�7�z��M��.:���ǿ���?��g����_�p+�_�VC��T�[x@X��WN�!���~��������)��O�K�C�	�����������>����5~����7��0<������?������K      *   �   x�����0��O�`�v<z5�� \HQc� j��-������.��}��e�ms�6����� _�/�9h���)dua0���
ݿ�����E=4���6��Oczq��<QJcO�k�j�z�tAq#�Kw�[��:��/�MT�\�qc[Vo�RK�I|�Xs��p�^�K��hU��p�6ũ�A�ZT&�cnH�ga      "   Y  x����n�0���gY��Ğ�7tp�5d�^�~�������8
|�)�?�P~4:�����e�F�Y��O��A�A#Jk�s�*#�U�x��`&?���K4ZKo�@�
�8�[w�W�j��&M�<��@�lؾߌ��k�iu&����h�C<�0Ë����)s(l� �Sh0��/?Nt��g��?;�,Zr�rR�i>�C�� �_��>U^.��,\����Y��-xj�|�� | '͒r~$蘮���$�Vi
Φ��c8�M%P�M�ǥZ�_T�!k����^��"/|i��?�E:˫nM%�B�,,RՕ� �������M�V�"-h�w1�<D�s# �\�Cp�˒ 6h�;A�-�#N@�z
BW\�
M	�0p�ϝ��IF�=�C��vu;���g�T�TU��`���R���8)܀E,VF�Y~�,�a�������=,�<䆂�u7Tu�ba��������(�*���]uۢ�Q-I�b����@�p}| 4��w�_2ŵ/���2gi�^����$�-��S�/*i;�S�IG|�����~
[Ͳ�c���U:��Q�]_M�ZƵ`H����0]gO��<I��9������4*�L\��g�=v���u��l�f�f�����y��=q/Uq�o��H�?«�!{Ժ"�b��8�]ܵ�eKe�= �}|�A�<���Q����O?�x脄k7�~bߺ��>��!u�i��_�
�K�I_n]��܍�U��{A�Y{�6p����)��N?�lq������W	��ڧ�&M����}�o=^@���x��1�a��t�w�K���<�=�|?�N� ���             x��}�v�H��s�+��̼1ax�DZ����]%�za�U��VZye�ng��G���7ԏ�3��-;��k�� $��3+\���n�~�O��o�����Ǜ�����������������ɛ�����a����4�_�n���&�7?��O���~���ۿ�|������0�vw�����J���������ds�e��w��Umkc��*LYUM���F�.�����0�Ea\�k<ZW�j�����4�+�=ޣ�����n����}�����tQ��p��a�'�py��M�vW����������?�<Z��<�{��(��Wӯ���:M������x��š�/�CU�w��k���ͯ�������2M�+��n�	���ǟ��?��������n��k�������o����8��?>��}r:2���#����t����>��o֚�ԥ���]Z��l]W�k]ғ�W��k|��_�/�����{�����r� +j?���� k���E|��!��ćl�S%>�Ow�#.��}���㮛
�����o����ɜ|�}|��t?���7�/����燇[x�p|�������7���3x-�[x��a��\1�ƺҖŴ**ۧ����W���J�	�&>?�?yh�=l������Y��	��ȅ�C��}>U����/D������<������ۻ;�Y���;-����{�`?�R��?}z'��(���_)U���-l^X*��uE����������`M|��w�ǎ�}e�@�׻�so������O��7�g.n>~�8���Eߋ�����B��;��a�Ѱq`39�`��h
C�����}��煠p#4��bz�����������G�̱�����,>�ݯ��{x0{QG�$no���������������������=?��������.��]g7�?�6������[o��)�ʖ��*U;7����ª�^)[��}�@����G�j\��ݣP���T�p[����K�~�*I�F��\|W�W�#�U��c�n��Mw�NN���f=�l߶ۿ�[�6��䏻nu5�>��N�nֵ�s�p���6���kW�v1��ۯ�i'������.���dٝ��8�X_����j'c�8X����zu���=Z8(P�N�)��J��jI悪�l�lZ4�hZ��%���M�SV��hw(�\w�=q?���W[��u�8�G-��U�X!�����=��)�����^���l�����w�����_�{F�E��=�_�'G���೦�Qd�ycA5����^�tU�ac�PN��}x_����av�Nl^�B+�i�c�a.�t���|�+~՝��t���n�ҦY��ص�9&��m7K&'~��7����n3_�ǧf���z�Y�#�w-l������W~����e��E���Ů�N������������E�n٭҉7�v���f=�tg(06��J~��|���o\u����vyɗ\��f"*�����7+�k���o��$?`���J���N~;���2*gE+;E��Qn�Lm3N���S2��2'J])�0�k��t[,�\��EW�t`X��v$�HUhh��AG������Ɛs��"��G�
�z`�����<��,�ң���W��#CL��%$ڽ������wO���D	�~�:�!��,�8o�����������RP� >`hݱrƖ5˙�s؎��n��l�n	қw��X��2Is�y��7����7�wk �l�0��C��a�ʂ3�.��ԍ3^ΗN�Fh�*�ҲNF��׮sA'�M�eO�O'��ǣ=o~�h���ů/}QJ���#/|Q*֋s�F���ѷh�m'�n�ٴ(�'���0����v��0 s>�t'���:�-�����v�o��u���^���������=�����4�ƪ�/Vڊ��*Ef�RE��O��9V���(r۵�=��R�^���t���m�����?�_�^�T��R�{9�yi^YX�AQ��yo'��W���#D��F�r��l歜|]ʂW�������\(
B��UwtCO��C�ߘ�!u4C�c]��+�.�,֛�u�B�l��e��[�Ǌ~u����ͽ3����n���r�%!p�9���$�+���%��k�
X��'�7�����lJ�j��`���׭�Y?,Y{˫��Օc��4K�.J���oQ�'6����t����J�K��y�����=l�:�Z��G��F+���ɼCO�W;���	�*����p���_���p���Ul*݄=�F���]{5GQڊ��νy^7eQ����V��FւW;���_�MU~ ձ�hK�����]{�^���/pk�.3�
�dv^�ђ㠟�-�L�<�E���kMKn��ݤKS�Q[�$�����m%R?�����*n�wS�wHo_|�&x[�!��)�y�)U��O8;Ib�f�(zd����.:Z����@6v��O��7Yt']�٢��h����ue��M3-�Z��.T���3N�e=6�LT��:.[��S0.�vk{������5Ż�2�t-�����J���o?�x?������A"�������~��fr1Y�x����=}��_���'��~��������������?�<��ś�6/���.���`,WT�2�-�q7t�
I}$��,�^| L��2�M�iT_h��bE苲@�E�H
�?�b�����#��G����&�-�w7�������奌����aeܾ�A_�������Bd���xB������ӥâ��ye�`B(�P��dZ��l7�~6�m,[迗kD����p6he�u����E0��y�p���M���U�����5�q������������W����r���	�$��`��[��L�������)Nl����a9�M�o�Q>�o(Ώ�MU?,�� C ΩkVne"�1�
'��p~R���UM�l��~վ����	��8>N����hn����|�mry�O�s'��n�=��gIrw�ϻɆp���O�PL�3�>�����ux�P����|��~kV�c�����s��يw��E�Ȼ�=F�m{-FzM뷑 ~��
������{w��⻃�9:�c4M>�}�>������;�)�` �bus�Z.��R�p
m�~�����I�N	�� Fu�+��u�on�n���Ȇ+x'����'�<�r?Y������;D+^Rm��A�Ҕ��\�vڊ�$N�
���	�e�F�T��I��Æ�s���MKL��o��Cx�q���<�v���������� ��<��������}����Iܓ����=�&�O�7FyP1��s�4�do��%[������6֧�q��^C�r�:�&�E��Q>��q|����e���y�>�0k����ɱ�Re*�f`���\��	S���~������I�)~�?��C2��p��Gn�����,��(J���]��ǒm�o;��?�gP�xx^9~Ph7V�F���A�z�JUu�eI{<8�M�i�"�Z��8a0�9��C��ў�=��������<xp�z(k�b�&�>�}���+�����-&K��Ȱǟ���O�����{D`�����g��|���bu���l������2�����O�7����x��2	'XطGN�����'į(~��5�%�3�r/3�6�¨tY�����Kp!��o�%Fk�����N�²�n��K��p�ڀ�E��j-�!���;]��e��+$�*k<��_q�:%�So�LG�+
�aX{8���?5ڟ�E���޶��
�"�yLY����ɲ�(�=�dѵ���0��Xr�M�g�ߴ'��Jg|bZ����|s֭��gJ�'���4��ť��,���dTk]��Zz����q���A�IJ8��04�AK�"$�
���x) �@@��v���V��b��+/_��={��04�\\+��b�׊�3&�����[ễ�s1v����3����uYBg�=]����
�R <�9?mau�em��i�d��    q�ȕ�[��b>s#�3�������F`�G����8G�d�d��>�Q�E`�1�� Q+�6�������]m��$��B,�4���JZ��A,r�>�t���k��[ E��&��w���b$�}el���ɼ��ty:��������ᓜ?����-�Y�U)��m��n���6� F��a��w!�|:���Z|���t��X��G���Ԋ$���v"�.�D����Ěj�E��/`�y�f�k�\��`��\�@�0E�|_�Y9�2�fy�_�{�����ѻ;B�f�K�7�G��USUKZ�M%I-��$�P�P���A�=�w��!�z�Ã�,�����w{��1��6W��[�#ۀt���a�K�M�]�I����ͮ��jf<ݛ"���֣�}�i������L�Ǔ�tMx�含#z7��✏�4Y3���i��V�ZR�e�*���Թ�+��9�eƳ$���Q��Ϣs��ߢb~�@�h����i�$����<�{"f%�v��u�N����M��vў��/�CodQ��b�6��������a�L��~�ɡP�Ģ��^����m?S���ָ�1A<#���,���U<.�4��	���]1:����s�g��s�ɞ�}M��c�}����x1��I��?rN�5�v�񧮨̔A/�t��2I�ё|��"梤T��\TR��ET%�2��41瘟�䠹֊��F��+���͆O�A\x**c���{�?��/�_��s�y��洛/�r����R�s�\�F�G����8R�՟�eD{��->MnО�߂ 0���84ͬV�02��P��82�D 7�]i����_�n���+�;#fɫ×����,
[VRp��'K���d%-	p���5Œ�r����W��IE�����S��+S�rb&_��ηb�<Q�?�$p��;�d��˛G�pCA������!�NⷅG�iW!H�Q�*Y�WU)Յ%'+*���o���m@�#��b�&K*�����zzU��0̀�������}�B���2US��]�k`�_��M���x�j�e�����a����G�i�A�e8�����\�_Y�*2�jS��h�����FIyb����}��@��u�/c�����s���whnr�W���tx��T*ڟK�����$���.��E�x�.�����e������E�����"fux�G[�K�CD�:*p�����u���p����IȒ�ň}���T멟~9a(1+>P�u��^a�>f�Hy�&�KX)��U�W��CA��-�@�`NRiO� ����l���`��`��~�c��.c��|w*�Al��@�� � ����M������v�}�j�Y77N���Y�	d��#�)�_M`�YB�XxNE�`�}Q��.j���,�rܸ�� +��v���v��[ٶK����)��pd5a�7�Y��Y����r%�`�Qo֧](�Z����ju=:��o�'b��K>�"��0��'f���\L�3��>�+En���G��ߛ��
���,�&0p��< ـ�Z��:q�\M����/C�#�����&����ʗ�.��q�Ҍ]�Dx(W6�r�ң
?�=^h�����CQ3Ƿ>��|�X��' �|vr��a��d�����z�Gtt���Sj��Ӹ��}���C�DS�d�K����A�[)q:�5�U��\X.o";#
�)�8od8t����s���	Q�?����r�%�{�&�fR�ԭ�2I���.{T��YQK���ڟF���|=v|�hWclw�Ѭ='�m8��y����&��I�6J�V;Et3�*���9f}ŕ6&�� ;!�u�~��@Ac���� ��Ѯd�	a*��Rt_b`[^��u���7�RŢ�B����
x���<���B�6NA��6�E}۳�L�$4=��u\\.],��S��Z��n2+�s��
\�$9��|����D��q�}dĭ`��0J�&�g[u=K|��"�rӯ~)2�i��w|e,��*�VHړu�7�b�9��2��O|����-�Ya��g3+=�� �E-*���
��dUU)Fh|A%�G��+�M�'{�I���JVœ�1�JK��%��~��Jn+~�z	fI�
{�\[~�Id!��x��>r�`:&�{S��`�QR�0�9a�1g����8U�c�긭(f�\-�_��$��x,6��=�c��y'x7�TJ=O*����q���d~�ɻL�4pv�CK�I�RM�_Gv*o��x�������|�a�LFf�X�/�6I1)#T�n�/,�Rs%�*�T�jL�x��J�؆0��Q�ּ}��qNҖ�K��H���eHa�%�8o�����:�x�w`��^����i8"L�'&Ba�\����US��w�-f����X8~��4a�WKo::��B�4~r��A��'%�F���kq�i��������H� j�R6Jȳ����\�$����0���W�i�F���T�s%H$��lS3�,����vf
_G ��3�t�o40�_�|��������G�e3���a���²� x3��̇�N�am
�l���m�d�zPP��$�CB�vѾhX�]�p�_���(U�)��M�"���e�zjoƸڊsIN1�E+eK�h�1:�-�����8#*U�%)xfA�d��T�|��sB���}���;�2ڠ_�YsP(��tK��j�x�;��R�j���X��c9���Ӽ�J��|s:�F����F�16�ۖ���o(�
�~X�6`D����8�I���
l�h��хA,��`Qa.9R����~��S�>AMY���&E,,9�z@��Ǜ�nIE�>��`x m@sqU����WM�#o#|Ӌ�E�۾��X�`Iy�FL+�!������VQ8���][L�֛��n��ȃ-j��C��fwr���q�q��v;���E��X���.)&��w�Q0j�c��J��s��QQz�1SS*�x�dT��xW0נ���;uUho�a�^��{�BA~#�J�:c��"�ě�m����1�xg�3_�S����
�!!׆�c�棞8̌>�:z���k�Af�~;��<��{�2 +`�\謍Dg�'lkY�;�ά�g��#Ĕ�t�)��%�VQN�N�֗��Gs�MTKc�PP7+�l� 
;���b]U�uU�2xD����S�e� �|Ԯ`�X��X��n ��9�R�le�b�BoLD'��T���@����l�ó����^䌞��4_�1z�՜*4�s����������n�a��@�Ǳ��s|VV�U@�7��8��#�/osM�V���0H7Ad_%lmC5��&Xi�/�L/����V%�
�H��>kSǗ������-L��&y?Xj�'��ւ��U���D����\�:Iib��_2<F�������˽_���PÆd��f}�����Ǘ��]�ܘ�/�����G#�NAcᏻ�t~u�]̼�J��,J7�byrFk�3��,�8�]���VT��$/��҈�#)��PV�W]� ��5|5��@?����t伀W.l~V6�D�>�(�� �ګC��-���s9�M����-�`ޥ�g�Zl��ݲ�V��@w��}�U�G���Q:������4k��o�a	؜����$�A�/�B~Z4�kK�-8�	���sy�D8�ġ��)FQ	�r�p�&#���G%��̹�G$�,�M7_]�cA/)=R�lH���4|:��O�~�wE��SEJ���{79[������S��i.ѧ��C��2ְ�v�}���6���
��Cʌ&�{�HYe��,C���|1��k��B��Jx�!n�w�s�	��awM������c��Hh�|?����t���1PR��+PD*TmN�1$��rx��Y{.�>�f�IޜL�Az�4ӹ��:�W���1��򻞼�o��sw	�q���.���`������(�|� ���w��p!�t���<�P6����#���/)�c� 5+��-;V�H�==��e�    0��I��vEAk�!�G�s�v��|�
ٝ��W��c���{�.�'���h(]k!�)��kp��S�	���z���4(��R������.]c�G���wB"
�)���wlLC�*O1
Y2�xB%D?F�Ψ5JVG��*�*��OZT���q��ç��m��s����-�,=ԁݪ��1�~='Ԝر��N�{���4QD'�b���ml�Zml贡��]!�HaT����m�KV
	�KꡠrN�T�����y�+�s
Z��ʨ�H�0���q��=G�-���>�0]rT
d��3j<9��4���s.��1_�&g@�W�p���.�3���)	l�Ȗ�d)�aX���D��CxU�ZaA��f���ռܛ��B���@ε�E��jT
\������8e�˻�ų�-���ȃ�9� ]�O�H��/N&���3"��p����U�Yx^��
$=&�K0"Y�-���.�[c��ʚ�Z�aL���z!aK�]1�Xͅ�W�;*	n�B��0憵�^�8GV�r ��/l�b���ञ�3��L���� &�
�hC��CY*yQK��fk�A��.���4�_�S��So��&r��lD�x�z� �;�K��b"�?�t�x�����:˶BJc�`�"P�)��-��n����B`�@s���y��p1KN�s��wM��P�8���-hC�0D��Ҕ%(�|��,q�*���]מN%���Zz�^\y��+[X�]{�|�8+Õ�y�T�����=�0g�Cг�Ң=,����#��#�fǱ69ꘄ�5Wñ���� I"��B;��jn��O�ݛ��s)ϸ��x�O�n��M�]J��щ��E�H� ih�����6���q)�D��#�)��	�˯B>�D뉂t�/j��(/$��&�p?`�X�Q���t�]dӥ����-�����ʳ�G�Z����((>W�b(�UQ;����a���çTQ�J�(N&Z5����mq�"�CH� �ڤ�u���%��d2��	��˚��G"���EIMA�_jW���1�
��I�$'��J���O,Q�	���kN��?��P�\E>R��z�
�y�n�F�PqNB�3��!����HoCEa��G<�Ҧ����(+l$�@���N��F�c�RJI��A����(gFO ��#��%@�G
[s�P�8��K%��p�l<�Zt$U�)n;=�v[�*��^Ѧ��E��s�ۄ�@O�@}���5�|�fP�����7��uH�,��2���SP�	�2Ԉ}��S����M$&]q��٣�z�0�n�� y;8+����x�XN$!Xz\�nZBe�݂Iy�\�4�揕�f::�&����uƧb��@�m�d>�%�C�n���C��H�s�a
����wEwf`���m.�C{ի*�S��QPш���E�,��?�7�["e�1.HC�N}�aP�s��gB۴S)�"v�&�9�ۥ���I}�Q_0|"��
>��[�VzY軹	%	O���UA��o��B�k�@���OD;�Ԛ�a�N9�`Aq��F�\�P6��M�y�����x�] ���N���1�\#l��f�R5�W2��D5 ����L^)��b�-�]�݊�#̹Ɠ4R���P:XT��}�O�Я���JV�*^�6T%��]2���6Y��~���)]G �?exg�퉬��9�#s���?o��ML�,"�{Y\�a�it���ѻO}��n�p���`��Nѹҍ�WEA>f=b��� a������JGR%�=%.M�A�_Q=�]��!Q �;^2|B��7j����f���f��m9�3D�:��Ń䕡����3Yr�g/S���+�,U���Z7�UMa��HŁU��Qe坒M����MJ!�^���d�:	�� �lx�m~Y�T|�Ƹ�8O����:p�6�Y������R���F���M$��N	_�+"��avgB�_74��a�{��b#���ᘙ�c8�����;���mw�R?��:U�h�\jX%U�O�:^�k1>���{��];>���#��8G��[�~�����c�_I���V���dZ.p3%9qgX�v�d*:Y���R���_�H��V�����L���ޫ>�������$Q�wk�C�ie�]mv`�g�%OP1��J.�_�xj�QDI
Z�b*���S\%+NӗX�g��)�$�](!�"�i�b�ب�!�(0�v4H�O�[�6��C�Y�paN��!e¼%F�"mi�XϥJ������o�q|D[�W�X_ǘ���#ڒ�-atqV���p��!vṖ�P��Cz��cwН8�i�)�_^y�\J�橶�9�J���������v��c��'�c߫�TB/�H#z� #�&�,�:���OB��������H�߳�����O8��������I�Б k�.���P4�U�D���vF9����pn&l������;n,M��r�N�A��r~�Vf�M t�ͻRU
�hb>Մ�UD��-��f`@$5��G1R~�|��Px�g�kd���#Y[ \#{ӻɻ�b�����(y�O�5�B!����&,��m�!�����&0��fO��ʗ�Sf��]f�x��x���	��cgrM�|m.D���v���t�¥8�J
O�
"�(!����xg�t5vזvQ��"���� %�&0�������P93�W�=(�L��J
k�>�
ªBzMq%)'�1e`��#���xaX�i��;�iU�<A��@8p�<��a��?�6������r�XU��<��%��U᝭�V'V�Ix-��d�3\���ճp�ڻ���ˀ�1E�n6��40তJ���ۛϞN��u%@w֨NZ(�)�T��ĜgD����#��2W��-�/�b8�	�kE`~���� aI�$�%�7)�#�eܭ�9��ڝt�/�yIl�$�3����ҩ�Wf<�D�;Ģ�RB�IYq2LX��pQ����e���>���@s��������0<�=��]��'�(;'��ء�;Ԁ:�~Z�� �:�hb��?�y3t�I���9	����PQ7��%Ep&�	�Vz՗N�Sf��fT$T)�'��d۱�5�:zn8�_V��@���t��o:�cHV̚��o��$�ʅ}T�?�I�����D!�|��
K+�B�������c�A�绀���:達l����D�����~�0���x=:ro4��S�u����<���W�]����;Sd�wdcf9Q:΁��|��4�*�n��-t�$�[�.=������
��jg��d�8�&T�r:��:�>�kc���A����ں�m��*��X�$�o;Rd�qSz��*`�3r�����s���g�]�#s�5�����*L�~~aB�*���W�F���W�;/��!(u��B!��
�Icb�U6� �tB%���-���<<+OB��ç�:z���hR��|Dj�?�<|��F�����nr�;���du�����3����S��6�2[X������V��)]J���\�Ȟ
��^K������1�l�|ݧ��_o~�}���McP���"��헝�S�[<��%!{/ ��HUx�FC<o������)n9��P,�Q�B��u���iU�o��#�l��W��c!�Čr$�|���B�A�OB3�ൔ+��oqe�T��n��i������] ���Xo��(�B�%�#d�ֳn�/�*Xa���=9/�1�T��w�P�|�5,ۓl��M�6م5 7��u�q��:���E��x��@���P��g�m"y�F�F{�HIDvn���z������bt�cK�7`R�w/G�:!I�J��O���������Mw�+T�4��w�2ߦ�5[����4şC�a�^H0���Ɣ�G���!�>�mU
��N�^7��6Iz���+�����m�A������ ��z�`XFI3���ϰ(�F:w��5[�Jz��RB��r��`:��j�X`���L�
}�-��|��&�S�KX@_�H�(�6k���^.���o��[�dl��`�k�9�<����[�u� �`��؁<�-�+��    E�Dt"��t�}�n6k���P�־ݶ�I"�	d�B+�Fr	�S>���ɚK4�|�8���t�-eJCk�)<���ڲ�o�F �[Ӗ׃7�����P-�?R>L��TZ
��5Y��JֹcP3��)$}��/k=���^4n����x���?o�<����H��B����٦=��\l/����W�L�=����)�O��cS��	�%�f��.כ|�G�dA�*���K�uQ�Zc�4b5M�O����8I��se�
\�ֿdx8:ȰJU�/�T65�@��yw�g�&�_o�j��,��8�(V�bj�rS%�E\�̅kD�����Ry���[j�pH{�I�rx�����h�`�������t�G+%bB�z�k0NVK��8��s~
�}z@B��:A�=(-�� 6`��m�L�^Is2����t�������n�[��iR��A���id�S���	m�|t��OT��c�V�2�y��~�8��nO@)�D_�O�V�.����������P׸�כ71�:�f0`zgi���|�N�#S���Lr1v�"���Ή�!׫�f��7�b��*�����+�*�@�8�]R*1�k��_	��վJ׬�6�>,a,mcW�1wD_Sqp�xtz�d-�/��|I<�* $�\vB
��y�C�R%!��^�qǴ�8n�|��1���q�.ސT�-�>�1z�J�G��)5������|�Lcf��:[���\N��Z�j�M%�1�0���pLyİF�B�(*abD�����v�=�|�ҫ�Jx8b)C.��:����ؾ5�s��l���+u�T������aQ�n�Ӄ&0���M�)6�58��T�2�k3(�	�XZE�g�N����=�׀�3�,T�M��c� �>Iye������'���CD�	�Qg�P��$\�R2��@{���N�:��#��/=���R��rR�b�<�K�K�?�\|�^]�`�=Q<BQ��{^A+�K���5"%G��Tu~\�
c�\CIn�e{��͸B�@����3�y
�ɥ��>ܮ����ތ�ʉ�*]��' �Z��2���_��C�L���=�#�aO{_��u��+3��d�?t���5�@���iހ���s�ZN{u���l{ݨ��%6$��<����
ܬ���������؄�P�nJ�rV\�W�Ԗ�m��3b��B�{���6@	o�e���(��CzQ�# �,�y����WRm%$�I�W���N�����Dz0������(Xup1��+�@�Y���l�ȝĴ�F�>~�\!�&��^
�����G	�4��,�P2�sh%����X@�{ZX<�� _~#����5D����h�"��H��%,5/$z-S�Qm�򜁤n�kD�mOƫ�9�;�l�õ���&�qQV���f��i�1�`��D�� �|R^�\�r1�<��B�A�N?c d�$���
ز��C�P��1��G0j@��h�m��4�ƫ�?��/p$�,���a�,Iw��+�nԓ���j���a<R$ǁ�p)Ԫ���(�Th��m^+D%�i�I�ۜ�@"�5���iz���v�>�O�EF���Sds�9-Rl��q���~��3�Q����r h9�PWh�&*l{��t�b}R�:��%�H;��=�K�V�����WrF津���/���Š�|ODƨG}]_��n��g)ۥ>��~r�ﱾ�i|�fQ���tY�52�ocF?�]��E��gZ
�Wt�mCz,�X�]!'vғ#\��η�SrJ�r�������2����W/��������4E�ԡ�WQK� .���̩"��T,�8:�|���u�n@�*��U�^S�=%zR�0<��+��d���0H��K�F���),��<{��J�ވ��',�����d���Yޯ�����miNn���
ֲ����_A��kka�0�M5�d��W��	�|��c�ɮF�ý��>	Nφb+��^#]5ڢ�Y�DR�B��sb�9K��' 5|�6�ѧS0�醷�i�������\�`����5�rL�D�K��R��&���}�1W��F2����� ����|���J��_0<��s"��=�7�e@�0��z,`��Y��zD��d�y��QNTF� q��2�B6g���E��҆�LIaE�{	���i�'`���V��V��h�������q���/UA}�	T<8[>8�cV조OdǴ�v�����)Ij�3�_	Tn�
/�_�h��-_��q܇%~Qi���q���"$&�ɏ�]�;�V�恙�D��ҹ*4;s.ĨU��\v����a֙X������P/��\�	�%i��T��
���Ȕ�.H�/���w�]�O���@fF���!�O��1E�!?
&�qׁ�S�B��̢	�9Dx$�;���s0'��9W�fL_�8��kj�Bd�)�L�=���֏�1�jWz���ȉ�$�������S�=�����V������,�%�� ��0��&���52��0�V�W 
fm�H^��×�?�i�b�'��|�4Rd�/
Y��a k�_uI�yL�UI�_��%��+�!���wh�QpT��h�vT�W,LS/zŅ��
���T&f8%��j��x=��c�^�IL�X�G4���df��W��'M �.�I铓á�]r;Au�+z�X	Q�d�<���%��bmd�O~����v�/���S��{��>�i���	�L��3^��>�h�w�rw��H�'���{%����� ���4|.��3b��>.h�DI��=ہ�:%�����ɡ�Dr,�Ny�ht�y��-�	𪨂ǎV�,(��%GM<��c���߈�f�uX������}<zx(գ����Ǜ�r���͝Q�#I������>4��_��ҤCPo^��t;�s'�r(|F�@�1�z�����{;����ӞL��t�Q�ۀooD��R>)��!X����9H�|�f˵n2)�ȹ&��+�W(�3õ45���u���Yr��	�8��-�����Fq��s�3DG���2��0%S��\*���B��d��t�ͽ!<9eǌ���,L�<J��\3AAr���w+���}�E)�
�����;��خkITQHTD⍺��^
��1j��k0v]mˢ�uZցJ��5G�&pJW�H��
�F���rF*���YCiurh9����۷�����Ѳ�{�|�f(�>hC�ϯOۥ�]Ω�&,��:����l���/=<z?^�d��)��ר)�ʲo8�(�!���c��n�-CmGZ�~-��|V���Dd�L����*#@|�p"��"
Vw��n�`]Z�;��!�;��̍�(vl�mp��|�a�j��+�N�Y�a]Gd��<<���b���*�� �==��  w>~�{imz�I�僣E�a�H���~p�ڑY���_`���]�a�nc���.��X�ݔG-im�㣜�ˮ�lw���L�%n� >�e{V)���y�y��_&g�]�tR �R��?��0!��]��v]
�2�����g˚��ZӀ�k��(������P��n�Ȱ,�p4�@��ݍ�W*����iJ:�6ZLh�5��Ӓ�Αb-ݪ��*瘜�A��@L�����?|��Ϫ�i�+�,B��Q�����<�L��BW�]���DemVsl�G��dfls�Wv���D�PfV榈t�*��I�Wo�ry�$Y�FN��ԗ�V��>W�u���!�*��.<X_���f1us�Դ
�3W�
6/��&�7��mz���
G���`��cV��g	��:4��}����z"w�5y��HT��z]	��M�І�$���V�)�?�}~Y
I�������(LE9�"��2�y*63����`j�f����E?��?�/YS�F]���7�u��x��_d����ѐ�%p0)���ὣ*N�M�>#� *=,�g��å�"0	+�H8_�0
[���Q������jn�;�[^"�z�br�K�hH�X�pM��ˆ�Ô���5x$ �  _��F<�8L���#q���6g�7�뵒r��}�̿W¯�?�!.3�4�QuEy���1|R�7��튔�&m�qF�:��gғ�r4�����X�R]џ�r�?�5�p�4}9��-�I4~�ؤ�ࢌ�	� �=�F������d�^sw���*�z`O,��[?�2����"���짱8f�˅��$�����,�,VR���@p�m�x��\`ѯ5��6��£UN���K����u]��㞕��Ԥ����Z��R?rd��b���'!4htv���K�SZ��+%�i$^�=#�(!Dlj1���qKc�|	�p�<��W�x�Q�����/J�T�Y�H�g�m=i.�_��ψc2��d��T��}���ݼ{ۦ����r��E�H��{g����w}�i	�ru]�n=aQ���.�>۔���h$�)DeB�����ke_1[��)�RSR�;����zy��������������_`(��#j��ܝ���ۜ(Tx��P�KZ�����)��Ԩ�k3���B�v(ͻL�T~��%�����]�@(�E`pT���IE��I>1Rw{uN�i�A�$�\�?9���Ӡg�9b��\r��t��S)�nRI��wb|�����d�,NK��v�^��4x����I{+|�!E}�����[�.8��ct��*��)�Izw���i�چK!�j��7���z���4���xOZ!�Mͪ��L܄��������6��M�)ll�^JĒ�E�5C5�l>����R 'L�����1AOs ��آ�� ���ޯ���;m_݄0O��l�d�|�-}��^���Q"���Q�OB݋���cXνǐ�G	��6�y�B��b-r�Q��bL׈A�t��%�.lxK�9��t�7ȟ�JR�F�V�|*�}�e��A`J� ժTR�͹�ʉ�k�VVzq�g�-�@�n�#:NgK��?��;�.pitKh:ή7��ִՠ5�|��>]ߐ��|�ko�wB��#��8�t�=p���d��H&I!#TN�}����2�~8��_`��ô%� 4��	��y�~�	���s�����8ɽ�a��A�$8�W��7����5�b��C�7ڲ;����r�j��Od5�������Wa0@RYZ?T���DfSM��Ok�njJ[c��R|�ن��r*��H��ВK�6�y�ll� ,c0�QPf��a�CrV�<��"'�R.�\�."^�5�M�\��Yi�;��?��<ON#��T���_Q8��@j�4���T>��Hg4������7�A�V6��N-U釩��b��w�p<�1@ �h_ե��B،@�dMj$Ѝ��{hÝ�{��(��C�7,Z�HPYW6V(��[�Fq!� =��"���ϧ�M�LĽ��&�==�lǎaM��c���m�A�7Q$�jJ�� ��/��C��gdeYXC�$�iAs`X���:;۽C.�5�P{�29�d�]mZ�kGm���Kl��M?)C�&2�`V<���X=�ZӎR�9��bw�>!����uKi�߄*��.#���#zW���$[U0�F9-��E�|b�jlE�3F	�E���Օ�TM(l-tm$N�\釮1^ˁ[�Q<��Z|�u����@����i!�����_=�i��7���>,�'�2H:㪩'+g#����IpT��ix��;9�������%F�A)R�g��
�4�����nW* ���ah_��駓Ħ�[^���Z�ݯ��E���i��|;��[yԵ�oNE���H#e�����XBGz^ϑ����;2&�z�%µ��|�����Ooo�n�n�li]�qq�re����>�L�O��|�ǌ�"+�b�_��?��_�<��%�����i��_�ϟ�h(�������1�z��|���-�'����k8�}��� ]��:�y���kw���^�z���~1�      $      x��\[�9��.�ek���%����RU[�ͬ�$�޹�� #�du�[��*x�   S!���_������_��(�_]y��%�X��%�Jk�G?���>�������},��y{�x{�XĽs���AP� A��O���\ �r�>P6^��	�j�����?ǔƫ� r�$�B���jj�ثO�DU�|�}���Jgc`�A��	���"XD��`U��k����?�}ǟ�W뫓%�:1}zŊah�͟_�!�����������V�0tzyM�d7A�����o��m!�	���E��PA9��E���g����!;t3����Ώ�o�,������_K�T���qƷo�A.�de�>v��\�{Y�p��Co��ڻ�u����	?�]���� h-�:�C�U*w'��/���	ONց
ߥ[Y�=�� G_)ܱ��0��q�� q���0�\#��?�|�^�SB졼��"�a�I��/N<4���,�V���pe���(�TР���Q�★��_*� L\4�����2Dc�ajN�&�����}e	�$AHH�W�P��H�{߼,1X,@X�=Q8�/%�&�$a���w�YHR��7&��J�v/F]D���>���I��n�K�y�� ����R����uT��ne�"��?��"ޯ?n�˘S����]���'>����^��~���Q�lۀ�i�t�'���"K�w�U߇�'&z�g}����1�Rkp91�f��5��d���b~������3�oG{��o_�&�;_^a�"We�~S >�h��`*�^}�rs�sĮ���\�a�={:����)`0B@�l�$��4)��`h�w��k�t��mh�04l�U���.�|��x��С/�YM}�t�2�y�`(XЁ ȡ�4����A3�0%
�%�/�/̌Q�lX�i�\h��t��M�y_�D��xTu�#��(P@K� U�$�t#6�Z�H<2�T%�	ե���D�_��$pzl�B�[�#Q�7��s������A��.���!^V��-�b��UꪅO�m���}C�T�����MB@���������Nqnsu7^��v�sO�pHC�QL'O�o�0v�d�Eއd=~`�}`}�nȵ���"���h��+�EB_a�*�hpR�]0x�1Ha�����GU�A�駴nY���
i��Ѕ�g�,��!y2�E���B��=�Nx�V�j��h��JF�ƣP����,��e��d@�d0�5��'Z$���և��;Y�S�Qݠ�)z���Su)j���K������;�����qD:�������D� ;�]�*y��$�Ƚ�E�dLˇU@��'kZD��*�:EO洈&Uh}��_PSVY���ɢѢ�
}�ɟ,j�*�Ч��ɢ�S���B�z����vU�SO����ى�,ʞb�"��d 㝲��}����.X�h&NDJ��g �s�N�-�b*��K~bQ�"�Ϯ�{}Ќ�5�ol��x���@B���k�G6at,��+��d?�m���	D��ًy���0����$2��$w�_s���������/�u������9]?r�.�N{��ʄ'�E-�B�Ƃ?�Qx?Ņ�9����
e�7w6Р��x.|��l�0Ҽ$����cF]-M��E�?���4�T�L�
����uc^���4iu��(ݙ��Q��(��՞C(��R����@�(1_���l���	 �{���6��P���F,�Sx4����u(��p'�s��> �!��b�]v�0�(������e�"�룓^j���^�M�.��Yt��-��������Жu�(kj."���<{���͆f��W��O
bC��s�m�uԊ�d��7�	��QC%��E�Q�H�H���f�t]B�.;�Ø�.�Iw� `xE�lt����>�"�2졯z`V�9���X�`�����_�����pj ��@Jb���ґ�ѐ22�&��2���c�:�K�e�@�,��	Q��
�ĸiRksx��͉�>֡+2N��E���<+��ؐ�-�B����0��E��>_ё�H�'��*?�5����=˛""�JgU�$-ò�2��Z��-�`�6���E�_ �gRt I9��� ��z=�����$�ZTy����<xl���n?G��ۻ��e����`C��ϥ�h������>al/��cA�-�S��>>�w�)9�=B��g�qa.�z�~��*g�mCS&pH�z=M�v�әi�	Ug��=����G�き������иn�v>J��"�A���{��uzG�f婃�MLy��Ǔ�ao]�=���C�+��
�����e��S��goKw`�9+�>�vm,k�IY���/�^>�
��ьf��T�#ʮ՝��GkÉ�BSV��i��"^r��*R#{/
�im���?������z�̎S��!� ������-����u퍠��&�P������`th���X��,w 
e��A��}e�h;�k�II����/ˈ�G�����cq�L��)8$��i�)�r����\5̃���&����Y�Y���I�	��Nm>B`s�ö�}�;��d}aj���|"jP�Eڤ>�b��ة��T�w͑��n"cT�B�E�d�z>�
�qT[�e�gwȘx���8��[�.a�ɾ��}/6��Y?]O��.�U�g�r=��	u��=�	ɡk�~��Gu��{L�4g����%����$�)��%ʽ���˾ԗ�n�S.�MBy�W�-r�o��\2_�����Z�_פO3�>?����5_��W��&�y�.Y��͒���à@�FY������sJ��8
��Ҙ��#T���M��D�h�(RY����.ȁ��1��9 �12�bgQ>� �YD�|:A��B�1 �"��R�#�W� ��@�l~�m_81�*cP@"=�')��	�B�e0�}��X�u�A!#�{n��OѭH�Ƞ��d`3�f���У0(�V������æ�ޕA �>�j�˨0�x5@�1��IR�=���A�âz�sVϊ<��Ju��G)'��� �8�`���囮�z��*k�A��Ea�.�"����Y�k��䜛EŦ�T@�9x�cKD�&���z�vV��+!!.JT�o�|�vӷH�ow�|�
��!��S����)��������ք��B����,6�frJ��`��igXW2��=N�H�YS�cd����*�mF�ͫNM�,b00F��Z�m]z�M�(=�c�P9|�4
�ڮix�p��\n�Ȣ�ǖ��;(S2�����߱����ﾙ�n
�Ԡ�+���F��=��:
� ��0`󎓠Wޛfٶ*�������� �T4!@Q��V�D^���\�y� I�g�@� ��g�d���Z��b2�!�BΗ���:R��{
^�R�\Q6ŐE�B�� ='�+��6��չ�Gϲ
>vo<�k�ʥ|
��Hu2�c"<,��=(�l}�aVהB�*�Iì�-ۺs� a��۠@�l�1
zi��V�"a��0(���ⶨSʹ�"+��H��"3��=����֦�h6�2)X��X�L���Ll����`Yq�zN�����ڑa��.���
N��նx˝
r��(�d�b�ڕ�R(P+
�O�Y6���~���]��(�7TUd`������|cKƀ��<c�m�ET�l��쑧�s���Tezxz�uoYvQ(x�0(���$"Sü�
��B���e�?k��2��z^�\JE( 3v��Q��`��.��� zUE( ���`�]�ދ���Wv7�.
��8(�/�D����.Q�^3(:C�eT����}�y9���2	O��-Ϝ$[��]4�h$u�ȯ�G�h�⺋��J��M�ȣ;��FRT����Zy��=$i{��n$]Ib$����ㅬ�f����$���� �{)�l+�4�^y!1�g �  $���}M��۝'�`�'��vK6��9�h�#w!QD���HZ3
���$��V��(bS�LB����0�N،֗�$�PJ6� �uB���e�X� �f����t�ӉJ6{�h�S�#����֐_E�{T���Mae#"e̾��]O���w�j$�Hx	C�����q�8�C1���8X���k��=<kE��M�nyˁ�~?�d�$�X�0H�6�g����K�fbm�š�����-/��+����|��H���
P���k8�T���Fa�I���j�l��;�����(���/���78���� a�zϓ��NaS,T-�c�K\h��]��>H�Ťhvbʴ�"n���xyf�NV�5r$�$r�A��ӷ�����2I��K'��,߿�F��n_����}ބ�
�"�������ҰW���>��t�a�P��ʴ��]�f��n�잓��C��W��W�>�Àj|��,�=��.���S3�*�� 	ϛ+NJuh��✒(�>MM����$;��t�A�n���"ފ���s�M���$A�t�;�k�m6�}��t���Ͳ*lj咐�v1�Z�/e5��y��qXrb���R��%鎃]kO���!�?����z�Ck�]�%j�7�>58���{px�޴�nu\c��m�g��������mcJ�mK���5�]%XM%Q�i�6�%
�X��$̓�m����35�"�F���c�ߤ�~+0�X|<D���(JK�H\��e��Y��S5
ƜFh���[P{��.0���4%ɓᵻ[�d����J�m�#�	O��9��K��vSl7���X6��逦H��~��!o�]����9���f��a,s�❛G�ŉ���^Y�ㆼL7XXuy��H�b'�F�X��@�(��Zd<٫.dZN+�GL�츮i#�T�%�V��6�߰۽�o�CK���0�P�z˭�nU��H�ܕ��WK�M���{�9�$���:H�nt}�8��UFJ��\3^���<����oKn��o8��A���f#���Z���$��	��ֱ��h�^�F�� $��g��L)�$7�b$EIP�	lvw��eo�m$�FR�Hx{�K��*��6��du�XFRN'����O�ߝ���8HhV���r����R%QL�$�i���xN'�ө]u����`#a��^�x1�C����2Slcu�,��I,6nwؓS��A�z��v�l��- ��Z�$��w	�-����N��0�E~r��L�ހ�sI|}�p�%�!��:X$�ݢ�4��a�	цb��L9��*�J|i�Rxm\HS���ԝ{ԏ,�ܾ����y�]�A��Ѿߊ�Hcci6�:i�˧,~���8���}�!7�rQ�q"R�Hk&ZGx���~����ŉ�^         r   x�U˱
�0 ���~A����kAp��r%M i�~�R��{�� ��>m\�F�%n�l��|����Ť!Z ��,��c��ǧm�6�$�y���1�J��
�C)u ��(�     