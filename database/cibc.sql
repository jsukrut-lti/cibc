PGDMP         8        
        z            cibc    14.1    14.1     s           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            t           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            u           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            v           1262    65979    cibc    DATABASE     h   CREATE DATABASE cibc WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE cibc;
                postgres    false            ?            1259    66048    accounts_customuser    TABLE     ?  CREATE TABLE public.accounts_customuser (
    id bigint NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL
);
 '   DROP TABLE public.accounts_customuser;
       public         heap    postgres    false            ?            1259    66059    accounts_customuser_groups    TABLE     ?   CREATE TABLE public.accounts_customuser_groups (
    id bigint NOT NULL,
    customuser_id bigint NOT NULL,
    group_id integer NOT NULL
);
 .   DROP TABLE public.accounts_customuser_groups;
       public         heap    postgres    false            ?            1259    66058 !   accounts_customuser_groups_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.accounts_customuser_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.accounts_customuser_groups_id_seq;
       public          postgres    false    222            w           0    0 !   accounts_customuser_groups_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.accounts_customuser_groups_id_seq OWNED BY public.accounts_customuser_groups.id;
          public          postgres    false    221            ?            1259    66047    accounts_customuser_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.accounts_customuser_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.accounts_customuser_id_seq;
       public          postgres    false    220            x           0    0    accounts_customuser_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.accounts_customuser_id_seq OWNED BY public.accounts_customuser.id;
          public          postgres    false    219            ?            1259    66066 $   accounts_customuser_user_permissions    TABLE     ?   CREATE TABLE public.accounts_customuser_user_permissions (
    id bigint NOT NULL,
    customuser_id bigint NOT NULL,
    permission_id integer NOT NULL
);
 8   DROP TABLE public.accounts_customuser_user_permissions;
       public         heap    postgres    false            ?            1259    66065 +   accounts_customuser_user_permissions_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.accounts_customuser_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 B   DROP SEQUENCE public.accounts_customuser_user_permissions_id_seq;
       public          postgres    false    224            y           0    0 +   accounts_customuser_user_permissions_id_seq    SEQUENCE OWNED BY     {   ALTER SEQUENCE public.accounts_customuser_user_permissions_id_seq OWNED BY public.accounts_customuser_user_permissions.id;
          public          postgres    false    223            ?            1259    66006 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         heap    postgres    false            ?            1259    66005    auth_group_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public          postgres    false    216            z           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public          postgres    false    215            ?            1259    66015    auth_group_permissions    TABLE     ?   CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         heap    postgres    false            ?            1259    66014    auth_group_permissions_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public          postgres    false    218            {           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public          postgres    false    217            ?            1259    65999    auth_permission    TABLE     ?   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         heap    postgres    false            ?            1259    65998    auth_permission_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public          postgres    false    214            |           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public          postgres    false    213            ?            1259    66123    authtoken_token    TABLE     ?   CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id bigint NOT NULL
);
 #   DROP TABLE public.authtoken_token;
       public         heap    postgres    false            ?            1259    66102    django_admin_log    TABLE     ?  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         heap    postgres    false            ?            1259    66101    django_admin_log_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public          postgres    false    226            }           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public          postgres    false    225            ?            1259    65990    django_content_type    TABLE     ?   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         heap    postgres    false            ?            1259    65989    django_content_type_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public          postgres    false    212            ~           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public          postgres    false    211            ?            1259    65981    django_migrations    TABLE     ?   CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         heap    postgres    false            ?            1259    65980    django_migrations_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public          postgres    false    210                       0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public          postgres    false    209            ?            1259    66273    django_session    TABLE     ?   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         heap    postgres    false            ?            1259    66283    django_site    TABLE     ?   CREATE TABLE public.django_site (
    id integer NOT NULL,
    domain character varying(100) NOT NULL,
    name character varying(50) NOT NULL
);
    DROP TABLE public.django_site;
       public         heap    postgres    false            ?            1259    66282    django_site_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.django_site_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.django_site_id_seq;
       public          postgres    false    250            ?           0    0    django_site_id_seq    SEQUENCE OWNED BY     I   ALTER SEQUENCE public.django_site_id_seq OWNED BY public.django_site.id;
          public          postgres    false    249            ?            1259    66168 /   insuranceProducts_assessmentquestionnairemaster    TABLE     ?  CREATE TABLE public."insuranceProducts_assessmentquestionnairemaster" (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    created_by character varying(300),
    modified_by character varying(300),
    assessment_id character varying(11) NOT NULL,
    assessment_details text NOT NULL,
    effective_start_date date NOT NULL,
    effective_end_date date NOT NULL,
    active boolean NOT NULL
);
 E   DROP TABLE public."insuranceProducts_assessmentquestionnairemaster";
       public         heap    postgres    false            ?            1259    66167 6   insuranceProducts_assessmentquestionnairemaster_id_seq    SEQUENCE     ?   CREATE SEQUENCE public."insuranceProducts_assessmentquestionnairemaster_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 O   DROP SEQUENCE public."insuranceProducts_assessmentquestionnairemaster_id_seq";
       public          postgres    false    233            ?           0    0 6   insuranceProducts_assessmentquestionnairemaster_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public."insuranceProducts_assessmentquestionnairemaster_id_seq" OWNED BY public."insuranceProducts_assessmentquestionnairemaster".id;
          public          postgres    false    232            ?            1259    66179    insuranceProducts_clientdetails    TABLE     /  CREATE TABLE public."insuranceProducts_clientdetails" (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    created_by character varying(300),
    modified_by character varying(300),
    client_id character varying(11) NOT NULL,
    client_name character varying(100) NOT NULL,
    client_email character varying(100) NOT NULL,
    client_phone character varying(100) NOT NULL,
    effective_start_date date NOT NULL,
    effective_end_date date NOT NULL,
    active boolean NOT NULL
);
 5   DROP TABLE public."insuranceProducts_clientdetails";
       public         heap    postgres    false            ?            1259    66178 &   insuranceProducts_clientdetails_id_seq    SEQUENCE     ?   CREATE SEQUENCE public."insuranceProducts_clientdetails_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ?   DROP SEQUENCE public."insuranceProducts_clientdetails_id_seq";
       public          postgres    false    235            ?           0    0 &   insuranceProducts_clientdetails_id_seq    SEQUENCE OWNED BY     u   ALTER SEQUENCE public."insuranceProducts_clientdetails_id_seq" OWNED BY public."insuranceProducts_clientdetails".id;
          public          postgres    false    234            ?            1259    66144 %   insuranceProducts_insurancediscussion    TABLE     W  CREATE TABLE public."insuranceProducts_insurancediscussion" (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    "primaryFirstName" character varying(50) NOT NULL,
    "primaryMiddleName" character varying(50) NOT NULL,
    "primaryLastName" character varying(50) NOT NULL,
    "primaryAge" smallint,
    "coFirstName" character varying(50) NOT NULL,
    "coMiddleName" character varying(50) NOT NULL,
    "coLastName" character varying(50) NOT NULL,
    "coAge" smallint,
    canada_provence character varying(2),
    "hoursWeekWorking" integer,
    "hasPartnerFinResponsibility" character varying(2),
    "hasChildrenFinResponsibility" character varying(2),
    "hasParentsFinResponsibility" character varying(2),
    "hasOthersFinResponsibility" character varying(2),
    "mortgageBalance" numeric(8,2),
    "mortgagePmtAmount" numeric(8,2),
    "mortgagePmtFrequency" character varying(2),
    "hlocLimit" numeric(8,2),
    "hlocBalance" numeric(8,2),
    "hlocMonthlyPmt" numeric(8,2),
    "personalLoanLimit" numeric(8,2),
    "personalAmortizationMonths" integer,
    "personalLoanBalance" numeric(8,2),
    "personalLoanMonthlyPmt" numeric(8,2),
    "personalPmtFrequency" character varying(2),
    "creditCardLimit" numeric(8,2),
    "creditCardBalance" numeric(8,2),
    "monthlyIncomeAfterTaxes" numeric(8,2),
    "totalMonthlyExpenses" numeric(8,2),
    "monthlyExpenseOtherCredit" numeric(8,2),
    "monthlyExpensePersonal" numeric(8,2),
    "monthlyExpenseOtherHousing" numeric(8,2),
    "monthlyExpensePropTaxFees" numeric(8,2),
    "monthlyExpenseOther" numeric(8,2),
    "totalSavings" numeric(8,2),
    "totalSavingsChequing" numeric(8,2),
    "totalSavingsTaxFreeAccts" numeric(8,2),
    "totalSavingsRegRetirement" numeric(8,2),
    "totalSavingsGuarantedInvestmentCerts" numeric(8,2),
    "totalSavingsOther" numeric(8,2),
    "lifeInsuranceLimit" numeric(8,2),
    "criticalIllnessLimit" numeric(8,2),
    "disabilityInsuranceMonthlyBenefit" numeric(8,2),
    "disabilityInsurancePercentCoveredByEmployer" smallint,
    "disabilityInsuranceUnknownEmployerCoverage" character varying(2),
    "lifeInsurancePremiumPerMonth" numeric(8,2),
    "criticalIllnessPremiumPerMonth" numeric(8,2),
    "disabilityPremiumPerMonth" numeric(8,2),
    "agentOverallPerceptionOfCustomerResp" character varying(20),
    "isRelatedToFinalizedSoldProduct" boolean NOT NULL,
    "discussionOutcomes" character varying(20),
    agent_id bigint NOT NULL,
    "insProduct_id" integer NOT NULL,
    "approxNetIncome" numeric(8,2),
    "coGender" character varying(2),
    created_by character varying(300),
    "currentApplicationPmt" numeric(8,2),
    "currentSection" character varying(40),
    modified_by character varying(300),
    "primaryGender" character varying(2),
    "savingsEmergencyFund" numeric(8,2),
    "sssavingsEmergencyFund" numeric(8,2),
    "totalExistingDebt" numeric(8,2),
    "totalMonthlyPmt" numeric(8,2),
    "totalSecuredAmt" numeric(8,2),
    "totalUnsecuredAmt" numeric(8,2),
    CONSTRAINT "insuranceProducts_insuranced_disabilityInsurancePercentCo_check" CHECK (("disabilityInsurancePercentCoveredByEmployer" >= 0)),
    CONSTRAINT "insuranceProducts_insurancediscussion_coAge_check" CHECK (("coAge" >= 0)),
    CONSTRAINT "insuranceProducts_insurancediscussion_primaryAge_check" CHECK (("primaryAge" >= 0))
);
 ;   DROP TABLE public."insuranceProducts_insurancediscussion";
       public         heap    postgres    false            ?            1259    66143 ,   insuranceProducts_insurancediscussion_id_seq    SEQUENCE     ?   CREATE SEQUENCE public."insuranceProducts_insurancediscussion_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 E   DROP SEQUENCE public."insuranceProducts_insurancediscussion_id_seq";
       public          postgres    false    231            ?           0    0 ,   insuranceProducts_insurancediscussion_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public."insuranceProducts_insurancediscussion_id_seq" OWNED BY public."insuranceProducts_insurancediscussion".id;
          public          postgres    false    230            ?            1259    66201 -   insuranceProducts_insurancenoneligiblecontent    TABLE     ?  CREATE TABLE public."insuranceProducts_insurancenoneligiblecontent" (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    created_by character varying(300),
    modified_by character varying(300),
    content text NOT NULL,
    effective_start_date date NOT NULL,
    effective_end_date date NOT NULL,
    active boolean NOT NULL
);
 C   DROP TABLE public."insuranceProducts_insurancenoneligiblecontent";
       public         heap    postgres    false            ?            1259    66200 4   insuranceProducts_insurancenoneligiblecontent_id_seq    SEQUENCE     ?   CREATE SEQUENCE public."insuranceProducts_insurancenoneligiblecontent_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 M   DROP SEQUENCE public."insuranceProducts_insurancenoneligiblecontent_id_seq";
       public          postgres    false    239            ?           0    0 4   insuranceProducts_insurancenoneligiblecontent_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public."insuranceProducts_insurancenoneligiblecontent_id_seq" OWNED BY public."insuranceProducts_insurancenoneligiblecontent".id;
          public          postgres    false    238            ?            1259    66210 )   insuranceProducts_insurancepreprocessdata    TABLE     ?  CREATE TABLE public."insuranceProducts_insurancepreprocessdata" (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    created_by character varying(300),
    modified_by character varying(300),
    application_number character varying(100) NOT NULL,
    status character varying(10) NOT NULL,
    data jsonb NOT NULL
);
 ?   DROP TABLE public."insuranceProducts_insurancepreprocessdata";
       public         heap    postgres    false            ?            1259    66209 0   insuranceProducts_insurancepreprocessdata_id_seq    SEQUENCE     ?   CREATE SEQUENCE public."insuranceProducts_insurancepreprocessdata_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 I   DROP SEQUENCE public."insuranceProducts_insurancepreprocessdata_id_seq";
       public          postgres    false    241            ?           0    0 0   insuranceProducts_insurancepreprocessdata_id_seq    SEQUENCE OWNED BY     ?   ALTER SEQUENCE public."insuranceProducts_insurancepreprocessdata_id_seq" OWNED BY public."insuranceProducts_insurancepreprocessdata".id;
          public          postgres    false    240            ?            1259    66137 "   insuranceProducts_insuranceproduct    TABLE     ?  CREATE TABLE public."insuranceProducts_insuranceproduct" (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    "productCode" character varying(50) NOT NULL,
    title character varying(200) NOT NULL,
    active boolean NOT NULL,
    created_by character varying(300),
    modified_by character varying(300),
    product_cibc_code character varying(50) NOT NULL,
    "creditProduct_code_id" integer NOT NULL
);
 8   DROP TABLE public."insuranceProducts_insuranceproduct";
       public         heap    postgres    false            ?            1259    66136 )   insuranceProducts_insuranceproduct_id_seq    SEQUENCE     ?   CREATE SEQUENCE public."insuranceProducts_insuranceproduct_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 B   DROP SEQUENCE public."insuranceProducts_insuranceproduct_id_seq";
       public          postgres    false    229            ?           0    0 )   insuranceProducts_insuranceproduct_id_seq    SEQUENCE OWNED BY     {   ALTER SEQUENCE public."insuranceProducts_insuranceproduct_id_seq" OWNED BY public."insuranceProducts_insuranceproduct".id;
          public          postgres    false    228            ?            1259    66190    insurance_credit_products    TABLE     ?  CREATE TABLE public.insurance_credit_products (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    created_by character varying(300),
    modified_by character varying(300),
    credit_product_code character varying(100) NOT NULL,
    credit_product_name character varying(200) NOT NULL,
    active boolean NOT NULL
);
 -   DROP TABLE public.insurance_credit_products;
       public         heap    postgres    false            ?            1259    66189     insurance_credit_products_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.insurance_credit_products_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.insurance_credit_products_id_seq;
       public          postgres    false    237            ?           0    0     insurance_credit_products_id_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.insurance_credit_products_id_seq OWNED BY public.insurance_credit_products.id;
          public          postgres    false    236            ?            1259    66241    insurance_eligibility_master    TABLE     ?  CREATE TABLE public.insurance_eligibility_master (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    created_by character varying(300),
    modified_by character varying(300),
    "minAge" smallint,
    "maxAge" smallint,
    residency character varying(50),
    effective_start_date date NOT NULL,
    effective_end_date date NOT NULL,
    active boolean NOT NULL,
    "insProduct_id" integer NOT NULL,
    occupation_id integer,
    CONSTRAINT "insurance_eligibility_master_maxAge_check" CHECK (("maxAge" >= 0)),
    CONSTRAINT "insurance_eligibility_master_minAge_check" CHECK (("minAge" >= 0))
);
 0   DROP TABLE public.insurance_eligibility_master;
       public         heap    postgres    false            ?            1259    66240 #   insurance_eligibility_master_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.insurance_eligibility_master_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 :   DROP SEQUENCE public.insurance_eligibility_master_id_seq;
       public          postgres    false    247            ?           0    0 #   insurance_eligibility_master_id_seq    SEQUENCE OWNED BY     k   ALTER SEQUENCE public.insurance_eligibility_master_id_seq OWNED BY public.insurance_eligibility_master.id;
          public          postgres    false    246            ?            1259    66219    occupation_master    TABLE     w  CREATE TABLE public.occupation_master (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    created_by character varying(300),
    modified_by character varying(300),
    occupation_code character varying(10) NOT NULL,
    occupation_name character varying(100) NOT NULL,
    active boolean NOT NULL
);
 %   DROP TABLE public.occupation_master;
       public         heap    postgres    false            ?            1259    66218    occupation_master_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.occupation_master_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.occupation_master_id_seq;
       public          postgres    false    243            ?           0    0    occupation_master_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.occupation_master_id_seq OWNED BY public.occupation_master.id;
          public          postgres    false    242            ?            1259    66228    province_residence_master    TABLE     ?  CREATE TABLE public.province_residence_master (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    created_by character varying(300),
    modified_by character varying(300),
    province character varying(3) NOT NULL,
    description character varying(100) NOT NULL,
    residency character varying(50),
    active boolean NOT NULL
);
 -   DROP TABLE public.province_residence_master;
       public         heap    postgres    false            ?            1259    66227     province_residence_master_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.province_residence_master_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.province_residence_master_id_seq;
       public          postgres    false    245            ?           0    0     province_residence_master_id_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.province_residence_master_id_seq OWNED BY public.province_residence_master.id;
          public          postgres    false    244            ?            1259    66293    stories_character    TABLE     ?  CREATE TABLE public.stories_character (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    "characterName" character varying(50) NOT NULL,
    backstory character varying(300) NOT NULL,
    "topType" character varying(50),
    "accessoriesType" character varying(50),
    "hatColor" character varying(50),
    "hairColor" character varying(50),
    "facialHairType" character varying(50),
    "facialHairColor" character varying(50),
    "clotheType" character varying(50),
    "clotheColor" character varying(50),
    "graphicType" character varying(50),
    "eyeType" character varying(50),
    "eyebrowType" character varying(50),
    "mouthType" character varying(50),
    "skinColor" character varying(50),
    "avatarImage" character varying(100),
    created_by character varying(300),
    modified_by character varying(300)
);
 %   DROP TABLE public.stories_character;
       public         heap    postgres    false            ?            1259    66292    stories_character_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.stories_character_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.stories_character_id_seq;
       public          postgres    false    252            ?           0    0    stories_character_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.stories_character_id_seq OWNED BY public.stories_character.id;
          public          postgres    false    251            ?            1259    66304    stories_objection    TABLE     ?  CREATE TABLE public.stories_objection (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    "objectionName" character varying(50) NOT NULL,
    "primaryIssueOrConcern" character varying(300) NOT NULL,
    status character varying(5),
    created_by character varying(300),
    modified_by character varying(300)
);
 %   DROP TABLE public.stories_objection;
       public         heap    postgres    false            ?            1259    66303    stories_objection_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.stories_objection_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.stories_objection_id_seq;
       public          postgres    false    254            ?           0    0    stories_objection_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.stories_objection_id_seq OWNED BY public.stories_objection.id;
          public          postgres    false    253                        1259    66313    stories_objectionhandle    TABLE     ?  CREATE TABLE public.stories_objectionhandle (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    "buttleName" character varying(50) NOT NULL,
    "buttleMessaging" character varying(300) NOT NULL,
    "buttleType" character varying(12),
    objection_id integer NOT NULL,
    created_by character varying(300),
    modified_by character varying(300)
);
 +   DROP TABLE public.stories_objectionhandle;
       public         heap    postgres    false            ?            1259    66312    stories_objectionhandle_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.stories_objectionhandle_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 5   DROP SEQUENCE public.stories_objectionhandle_id_seq;
       public          postgres    false    256            ?           0    0    stories_objectionhandle_id_seq    SEQUENCE OWNED BY     a   ALTER SEQUENCE public.stories_objectionhandle_id_seq OWNED BY public.stories_objectionhandle.id;
          public          postgres    false    255            
           1259    66355 #   stories_objectionhandlestatstracker    TABLE     /  CREATE TABLE public.stories_objectionhandlestatstracker (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    "hasMessagingTransmitted" boolean NOT NULL,
    "messagingTransmissionType" character varying(20) NOT NULL,
    "agentPerceptionOfCustomerResp" character varying(20) NOT NULL,
    agent_id bigint NOT NULL,
    "insuranceDiscussion_id" integer NOT NULL,
    "objectionHandle_id" integer NOT NULL,
    created_by character varying(300),
    modified_by character varying(300)
);
 7   DROP TABLE public.stories_objectionhandlestatstracker;
       public         heap    postgres    false            	           1259    66354 *   stories_objectionhandlestatstracker_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.stories_objectionhandlestatstracker_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 A   DROP SEQUENCE public.stories_objectionhandlestatstracker_id_seq;
       public          postgres    false    266            ?           0    0 *   stories_objectionhandlestatstracker_id_seq    SEQUENCE OWNED BY     y   ALTER SEQUENCE public.stories_objectionhandlestatstracker_id_seq OWNED BY public.stories_objectionhandlestatstracker.id;
          public          postgres    false    265                       1259    66348    stories_objectioonstatstracker    TABLE     "  CREATE TABLE public.stories_objectioonstatstracker (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    "hasMessagingTransmitted" boolean NOT NULL,
    "messagingTransmissionType" character varying(20) NOT NULL,
    "agentPerceptionOfCustomerResp" character varying(20) NOT NULL,
    agent_id bigint NOT NULL,
    "insuranceDiscussion_id" integer NOT NULL,
    objection_id integer NOT NULL,
    created_by character varying(300),
    modified_by character varying(300)
);
 2   DROP TABLE public.stories_objectioonstatstracker;
       public         heap    postgres    false                       1259    66347 %   stories_objectioonstatstracker_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.stories_objectioonstatstracker_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 <   DROP SEQUENCE public.stories_objectioonstatstracker_id_seq;
       public          postgres    false    264            ?           0    0 %   stories_objectioonstatstracker_id_seq    SEQUENCE OWNED BY     o   ALTER SEQUENCE public.stories_objectioonstatstracker_id_seq OWNED BY public.stories_objectioonstatstracker.id;
          public          postgres    false    263                       1259    66322    stories_story    TABLE     ,  CREATE TABLE public.stories_story (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    "storyName" character varying(50) NOT NULL,
    summary character varying(300) NOT NULL,
    introduction character varying(300) NOT NULL,
    middle character varying(300) NOT NULL,
    conclusion character varying(300) NOT NULL,
    "keyInsights" character varying(300) NOT NULL,
    status character varying(5),
    created_by character varying(300),
    modified_by character varying(300)
);
 !   DROP TABLE public.stories_story;
       public         heap    postgres    false                       1259    66321    stories_story_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.stories_story_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.stories_story_id_seq;
       public          postgres    false    258            ?           0    0    stories_story_id_seq    SEQUENCE OWNED BY     M   ALTER SEQUENCE public.stories_story_id_seq OWNED BY public.stories_story.id;
          public          postgres    false    257                       1259    66340    stories_storycharacter    TABLE     ?  CREATE TABLE public.stories_storycharacter (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    "priorityOrder" smallint,
    character_id integer NOT NULL,
    story_id integer NOT NULL,
    created_by character varying(300),
    modified_by character varying(300),
    CONSTRAINT "stories_storycharacter_priorityOrder_check" CHECK (("priorityOrder" >= 0))
);
 *   DROP TABLE public.stories_storycharacter;
       public         heap    postgres    false                       1259    66339    stories_storycharacter_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.stories_storycharacter_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.stories_storycharacter_id_seq;
       public          postgres    false    262            ?           0    0    stories_storycharacter_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.stories_storycharacter_id_seq OWNED BY public.stories_storycharacter.id;
          public          postgres    false    261                       1259    66333    stories_storystatstracker    TABLE       CREATE TABLE public.stories_storystatstracker (
    id integer NOT NULL,
    created timestamp with time zone NOT NULL,
    modified timestamp with time zone NOT NULL,
    "hasMessagingTransmitted" boolean NOT NULL,
    "messagingTransmissionType" character varying(20) NOT NULL,
    "agentPerceptionOfCustomerResp" character varying(20) NOT NULL,
    agent_id bigint NOT NULL,
    "insuranceDiscussion_id" integer NOT NULL,
    story_id integer NOT NULL,
    created_by character varying(300),
    modified_by character varying(300)
);
 -   DROP TABLE public.stories_storystatstracker;
       public         heap    postgres    false                       1259    66332     stories_storystatstracker_id_seq    SEQUENCE     ?   CREATE SEQUENCE public.stories_storystatstracker_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 7   DROP SEQUENCE public.stories_storystatstracker_id_seq;
       public          postgres    false    260            ?           0    0     stories_storystatstracker_id_seq    SEQUENCE OWNED BY     e   ALTER SEQUENCE public.stories_storystatstracker_id_seq OWNED BY public.stories_storystatstracker.id;
          public          postgres    false    259            ?           2604    66051    accounts_customuser id    DEFAULT     ?   ALTER TABLE ONLY public.accounts_customuser ALTER COLUMN id SET DEFAULT nextval('public.accounts_customuser_id_seq'::regclass);
 E   ALTER TABLE public.accounts_customuser ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    220    220            ?           2604    66062    accounts_customuser_groups id    DEFAULT     ?   ALTER TABLE ONLY public.accounts_customuser_groups ALTER COLUMN id SET DEFAULT nextval('public.accounts_customuser_groups_id_seq'::regclass);
 L   ALTER TABLE public.accounts_customuser_groups ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    222    221    222            ?           2604    66069 '   accounts_customuser_user_permissions id    DEFAULT     ?   ALTER TABLE ONLY public.accounts_customuser_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.accounts_customuser_user_permissions_id_seq'::regclass);
 V   ALTER TABLE public.accounts_customuser_user_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    223    224    224            ?           2604    66009    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    216    216            ?           2604    66018    auth_group_permissions id    DEFAULT     ?   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    217    218            ?           2604    66002    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    213    214            ?           2604    66105    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    225    226            ?           2604    65993    django_content_type id    DEFAULT     ?   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    211    212    212            ?           2604    65984    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    210    209    210                       2604    66286    django_site id    DEFAULT     p   ALTER TABLE ONLY public.django_site ALTER COLUMN id SET DEFAULT nextval('public.django_site_id_seq'::regclass);
 =   ALTER TABLE public.django_site ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    249    250    250            ?           2604    66171 2   insuranceProducts_assessmentquestionnairemaster id    DEFAULT     ?   ALTER TABLE ONLY public."insuranceProducts_assessmentquestionnairemaster" ALTER COLUMN id SET DEFAULT nextval('public."insuranceProducts_assessmentquestionnairemaster_id_seq"'::regclass);
 c   ALTER TABLE public."insuranceProducts_assessmentquestionnairemaster" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    232    233    233            ?           2604    66182 "   insuranceProducts_clientdetails id    DEFAULT     ?   ALTER TABLE ONLY public."insuranceProducts_clientdetails" ALTER COLUMN id SET DEFAULT nextval('public."insuranceProducts_clientdetails_id_seq"'::regclass);
 S   ALTER TABLE public."insuranceProducts_clientdetails" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    234    235    235            ?           2604    66147 (   insuranceProducts_insurancediscussion id    DEFAULT     ?   ALTER TABLE ONLY public."insuranceProducts_insurancediscussion" ALTER COLUMN id SET DEFAULT nextval('public."insuranceProducts_insurancediscussion_id_seq"'::regclass);
 Y   ALTER TABLE public."insuranceProducts_insurancediscussion" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    231    230    231            ?           2604    66204 0   insuranceProducts_insurancenoneligiblecontent id    DEFAULT     ?   ALTER TABLE ONLY public."insuranceProducts_insurancenoneligiblecontent" ALTER COLUMN id SET DEFAULT nextval('public."insuranceProducts_insurancenoneligiblecontent_id_seq"'::regclass);
 a   ALTER TABLE public."insuranceProducts_insurancenoneligiblecontent" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    239    238    239            ?           2604    66213 ,   insuranceProducts_insurancepreprocessdata id    DEFAULT     ?   ALTER TABLE ONLY public."insuranceProducts_insurancepreprocessdata" ALTER COLUMN id SET DEFAULT nextval('public."insuranceProducts_insurancepreprocessdata_id_seq"'::regclass);
 ]   ALTER TABLE public."insuranceProducts_insurancepreprocessdata" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    240    241    241            ?           2604    66140 %   insuranceProducts_insuranceproduct id    DEFAULT     ?   ALTER TABLE ONLY public."insuranceProducts_insuranceproduct" ALTER COLUMN id SET DEFAULT nextval('public."insuranceProducts_insuranceproduct_id_seq"'::regclass);
 V   ALTER TABLE public."insuranceProducts_insuranceproduct" ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    229    228    229            ?           2604    66193    insurance_credit_products id    DEFAULT     ?   ALTER TABLE ONLY public.insurance_credit_products ALTER COLUMN id SET DEFAULT nextval('public.insurance_credit_products_id_seq'::regclass);
 K   ALTER TABLE public.insurance_credit_products ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    237    236    237                       2604    66244    insurance_eligibility_master id    DEFAULT     ?   ALTER TABLE ONLY public.insurance_eligibility_master ALTER COLUMN id SET DEFAULT nextval('public.insurance_eligibility_master_id_seq'::regclass);
 N   ALTER TABLE public.insurance_eligibility_master ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    247    246    247            ?           2604    66222    occupation_master id    DEFAULT     |   ALTER TABLE ONLY public.occupation_master ALTER COLUMN id SET DEFAULT nextval('public.occupation_master_id_seq'::regclass);
 C   ALTER TABLE public.occupation_master ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    242    243    243                        2604    66231    province_residence_master id    DEFAULT     ?   ALTER TABLE ONLY public.province_residence_master ALTER COLUMN id SET DEFAULT nextval('public.province_residence_master_id_seq'::regclass);
 K   ALTER TABLE public.province_residence_master ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    244    245    245                       2604    66296    stories_character id    DEFAULT     |   ALTER TABLE ONLY public.stories_character ALTER COLUMN id SET DEFAULT nextval('public.stories_character_id_seq'::regclass);
 C   ALTER TABLE public.stories_character ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    251    252    252                       2604    66307    stories_objection id    DEFAULT     |   ALTER TABLE ONLY public.stories_objection ALTER COLUMN id SET DEFAULT nextval('public.stories_objection_id_seq'::regclass);
 C   ALTER TABLE public.stories_objection ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    254    253    254                       2604    66316    stories_objectionhandle id    DEFAULT     ?   ALTER TABLE ONLY public.stories_objectionhandle ALTER COLUMN id SET DEFAULT nextval('public.stories_objectionhandle_id_seq'::regclass);
 I   ALTER TABLE public.stories_objectionhandle ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    255    256    256                       2604    66358 &   stories_objectionhandlestatstracker id    DEFAULT     ?   ALTER TABLE ONLY public.stories_objectionhandlestatstracker ALTER COLUMN id SET DEFAULT nextval('public.stories_objectionhandlestatstracker_id_seq'::regclass);
 U   ALTER TABLE public.stories_objectionhandlestatstracker ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    266    265    266                       2604    66351 !   stories_objectioonstatstracker id    DEFAULT     ?   ALTER TABLE ONLY public.stories_objectioonstatstracker ALTER COLUMN id SET DEFAULT nextval('public.stories_objectioonstatstracker_id_seq'::regclass);
 P   ALTER TABLE public.stories_objectioonstatstracker ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    264    263    264                       2604    66325    stories_story id    DEFAULT     t   ALTER TABLE ONLY public.stories_story ALTER COLUMN id SET DEFAULT nextval('public.stories_story_id_seq'::regclass);
 ?   ALTER TABLE public.stories_story ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    257    258    258            
           2604    66343    stories_storycharacter id    DEFAULT     ?   ALTER TABLE ONLY public.stories_storycharacter ALTER COLUMN id SET DEFAULT nextval('public.stories_storycharacter_id_seq'::regclass);
 H   ALTER TABLE public.stories_storycharacter ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    262    261    262            	           2604    66336    stories_storystatstracker id    DEFAULT     ?   ALTER TABLE ONLY public.stories_storystatstracker ALTER COLUMN id SET DEFAULT nextval('public.stories_storystatstracker_id_seq'::regclass);
 K   ALTER TABLE public.stories_storystatstracker ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    260    259    260            B          0    66048    accounts_customuser 
   TABLE DATA           ?   COPY public.accounts_customuser (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) FROM stdin;
    public          postgres    false    220   1?      D          0    66059    accounts_customuser_groups 
   TABLE DATA           Q   COPY public.accounts_customuser_groups (id, customuser_id, group_id) FROM stdin;
    public          postgres    false    222   U?      F          0    66066 $   accounts_customuser_user_permissions 
   TABLE DATA           `   COPY public.accounts_customuser_user_permissions (id, customuser_id, permission_id) FROM stdin;
    public          postgres    false    224   x?      >          0    66006 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          postgres    false    216   ??      @          0    66015    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          postgres    false    218   ??      <          0    65999    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          postgres    false    214   ??      I          0    66123    authtoken_token 
   TABLE DATA           @   COPY public.authtoken_token (key, created, user_id) FROM stdin;
    public          postgres    false    227   ??      H          0    66102    django_admin_log 
   TABLE DATA           ?   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          postgres    false    226   ??      :          0    65990    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          postgres    false    212   ??      8          0    65981    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          postgres    false    210   ??      ^          0    66273    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          postgres    false    248   ??      `          0    66283    django_site 
   TABLE DATA           7   COPY public.django_site (id, domain, name) FROM stdin;
    public          postgres    false    250   ?      O          0    66168 /   insuranceProducts_assessmentquestionnairemaster 
   TABLE DATA           ?   COPY public."insuranceProducts_assessmentquestionnairemaster" (id, created, modified, created_by, modified_by, assessment_id, assessment_details, effective_start_date, effective_end_date, active) FROM stdin;
    public          postgres    false    233   1?      Q          0    66179    insuranceProducts_clientdetails 
   TABLE DATA           ?   COPY public."insuranceProducts_clientdetails" (id, created, modified, created_by, modified_by, client_id, client_name, client_email, client_phone, effective_start_date, effective_end_date, active) FROM stdin;
    public          postgres    false    235   6?      M          0    66144 %   insuranceProducts_insurancediscussion 
   TABLE DATA           f  COPY public."insuranceProducts_insurancediscussion" (id, created, modified, "primaryFirstName", "primaryMiddleName", "primaryLastName", "primaryAge", "coFirstName", "coMiddleName", "coLastName", "coAge", canada_provence, "hoursWeekWorking", "hasPartnerFinResponsibility", "hasChildrenFinResponsibility", "hasParentsFinResponsibility", "hasOthersFinResponsibility", "mortgageBalance", "mortgagePmtAmount", "mortgagePmtFrequency", "hlocLimit", "hlocBalance", "hlocMonthlyPmt", "personalLoanLimit", "personalAmortizationMonths", "personalLoanBalance", "personalLoanMonthlyPmt", "personalPmtFrequency", "creditCardLimit", "creditCardBalance", "monthlyIncomeAfterTaxes", "totalMonthlyExpenses", "monthlyExpenseOtherCredit", "monthlyExpensePersonal", "monthlyExpenseOtherHousing", "monthlyExpensePropTaxFees", "monthlyExpenseOther", "totalSavings", "totalSavingsChequing", "totalSavingsTaxFreeAccts", "totalSavingsRegRetirement", "totalSavingsGuarantedInvestmentCerts", "totalSavingsOther", "lifeInsuranceLimit", "criticalIllnessLimit", "disabilityInsuranceMonthlyBenefit", "disabilityInsurancePercentCoveredByEmployer", "disabilityInsuranceUnknownEmployerCoverage", "lifeInsurancePremiumPerMonth", "criticalIllnessPremiumPerMonth", "disabilityPremiumPerMonth", "agentOverallPerceptionOfCustomerResp", "isRelatedToFinalizedSoldProduct", "discussionOutcomes", agent_id, "insProduct_id", "approxNetIncome", "coGender", created_by, "currentApplicationPmt", "currentSection", modified_by, "primaryGender", "savingsEmergencyFund", "sssavingsEmergencyFund", "totalExistingDebt", "totalMonthlyPmt", "totalSecuredAmt", "totalUnsecuredAmt") FROM stdin;
    public          postgres    false    231   S?      U          0    66201 -   insuranceProducts_insurancenoneligiblecontent 
   TABLE DATA           ?   COPY public."insuranceProducts_insurancenoneligiblecontent" (id, created, modified, created_by, modified_by, content, effective_start_date, effective_end_date, active) FROM stdin;
    public          postgres    false    239   p?      W          0    66210 )   insuranceProducts_insurancepreprocessdata 
   TABLE DATA           ?   COPY public."insuranceProducts_insurancepreprocessdata" (id, created, modified, created_by, modified_by, application_number, status, data) FROM stdin;
    public          postgres    false    241   U?      K          0    66137 "   insuranceProducts_insuranceproduct 
   TABLE DATA           ?   COPY public."insuranceProducts_insuranceproduct" (id, created, modified, "productCode", title, active, created_by, modified_by, product_cibc_code, "creditProduct_code_id") FROM stdin;
    public          postgres    false    229   ?      S          0    66190    insurance_credit_products 
   TABLE DATA           ?   COPY public.insurance_credit_products (id, created, modified, created_by, modified_by, credit_product_code, credit_product_name, active) FROM stdin;
    public          postgres    false    237   ??      ]          0    66241    insurance_eligibility_master 
   TABLE DATA           ?   COPY public.insurance_eligibility_master (id, created, modified, created_by, modified_by, "minAge", "maxAge", residency, effective_start_date, effective_end_date, active, "insProduct_id", occupation_id) FROM stdin;
    public          postgres    false    247   U?      Y          0    66219    occupation_master 
   TABLE DATA           ?   COPY public.occupation_master (id, created, modified, created_by, modified_by, occupation_code, occupation_name, active) FROM stdin;
    public          postgres    false    243   c?      [          0    66228    province_residence_master 
   TABLE DATA           ?   COPY public.province_residence_master (id, created, modified, created_by, modified_by, province, description, residency, active) FROM stdin;
    public          postgres    false    245   ??      b          0    66293    stories_character 
   TABLE DATA           B  COPY public.stories_character (id, created, modified, "characterName", backstory, "topType", "accessoriesType", "hatColor", "hairColor", "facialHairType", "facialHairColor", "clotheType", "clotheColor", "graphicType", "eyeType", "eyebrowType", "mouthType", "skinColor", "avatarImage", created_by, modified_by) FROM stdin;
    public          postgres    false    252   ??      d          0    66304    stories_objection 
   TABLE DATA           ?   COPY public.stories_objection (id, created, modified, "objectionName", "primaryIssueOrConcern", status, created_by, modified_by) FROM stdin;
    public          postgres    false    254   ??      f          0    66313    stories_objectionhandle 
   TABLE DATA           ?   COPY public.stories_objectionhandle (id, created, modified, "buttleName", "buttleMessaging", "buttleType", objection_id, created_by, modified_by) FROM stdin;
    public          postgres    false    256   w?      p          0    66355 #   stories_objectionhandlestatstracker 
   TABLE DATA              COPY public.stories_objectionhandlestatstracker (id, created, modified, "hasMessagingTransmitted", "messagingTransmissionType", "agentPerceptionOfCustomerResp", agent_id, "insuranceDiscussion_id", "objectionHandle_id", created_by, modified_by) FROM stdin;
    public          postgres    false    266   B?      n          0    66348    stories_objectioonstatstracker 
   TABLE DATA           ?   COPY public.stories_objectioonstatstracker (id, created, modified, "hasMessagingTransmitted", "messagingTransmissionType", "agentPerceptionOfCustomerResp", agent_id, "insuranceDiscussion_id", objection_id, created_by, modified_by) FROM stdin;
    public          postgres    false    264   _?      h          0    66322    stories_story 
   TABLE DATA           ?   COPY public.stories_story (id, created, modified, "storyName", summary, introduction, middle, conclusion, "keyInsights", status, created_by, modified_by) FROM stdin;
    public          postgres    false    258   |?      l          0    66340    stories_storycharacter 
   TABLE DATA           ?   COPY public.stories_storycharacter (id, created, modified, "priorityOrder", character_id, story_id, created_by, modified_by) FROM stdin;
    public          postgres    false    262   ?      j          0    66333    stories_storystatstracker 
   TABLE DATA           ?   COPY public.stories_storystatstracker (id, created, modified, "hasMessagingTransmitted", "messagingTransmissionType", "agentPerceptionOfCustomerResp", agent_id, "insuranceDiscussion_id", story_id, created_by, modified_by) FROM stdin;
    public          postgres    false    260   #?      ?           0    0 !   accounts_customuser_groups_id_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public.accounts_customuser_groups_id_seq', 1, true);
          public          postgres    false    221            ?           0    0    accounts_customuser_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.accounts_customuser_id_seq', 2, true);
          public          postgres    false    219            ?           0    0 +   accounts_customuser_user_permissions_id_seq    SEQUENCE SET     Z   SELECT pg_catalog.setval('public.accounts_customuser_user_permissions_id_seq', 1, false);
          public          postgres    false    223            ?           0    0    auth_group_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.auth_group_id_seq', 3, true);
          public          postgres    false    215            ?           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
          public          postgres    false    217            ?           0    0    auth_permission_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_permission_id_seq', 108, true);
          public          postgres    false    213            ?           0    0    django_admin_log_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 5, true);
          public          postgres    false    225            ?           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 27, true);
          public          postgres    false    211            ?           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 37, true);
          public          postgres    false    209            ?           0    0    django_site_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.django_site_id_seq', 2, true);
          public          postgres    false    249            ?           0    0 6   insuranceProducts_assessmentquestionnairemaster_id_seq    SEQUENCE SET     g   SELECT pg_catalog.setval('public."insuranceProducts_assessmentquestionnairemaster_id_seq"', 1, false);
          public          postgres    false    232            ?           0    0 &   insuranceProducts_clientdetails_id_seq    SEQUENCE SET     W   SELECT pg_catalog.setval('public."insuranceProducts_clientdetails_id_seq"', 1, false);
          public          postgres    false    234            ?           0    0 ,   insuranceProducts_insurancediscussion_id_seq    SEQUENCE SET     ]   SELECT pg_catalog.setval('public."insuranceProducts_insurancediscussion_id_seq"', 1, false);
          public          postgres    false    230            ?           0    0 4   insuranceProducts_insurancenoneligiblecontent_id_seq    SEQUENCE SET     e   SELECT pg_catalog.setval('public."insuranceProducts_insurancenoneligiblecontent_id_seq"', 1, false);
          public          postgres    false    238            ?           0    0 0   insuranceProducts_insurancepreprocessdata_id_seq    SEQUENCE SET     `   SELECT pg_catalog.setval('public."insuranceProducts_insurancepreprocessdata_id_seq"', 2, true);
          public          postgres    false    240            ?           0    0 )   insuranceProducts_insuranceproduct_id_seq    SEQUENCE SET     Z   SELECT pg_catalog.setval('public."insuranceProducts_insuranceproduct_id_seq"', 1, false);
          public          postgres    false    228            ?           0    0     insurance_credit_products_id_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public.insurance_credit_products_id_seq', 1, false);
          public          postgres    false    236            ?           0    0 #   insurance_eligibility_master_id_seq    SEQUENCE SET     R   SELECT pg_catalog.setval('public.insurance_eligibility_master_id_seq', 1, false);
          public          postgres    false    246            ?           0    0    occupation_master_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.occupation_master_id_seq', 1, false);
          public          postgres    false    242            ?           0    0     province_residence_master_id_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public.province_residence_master_id_seq', 1, false);
          public          postgres    false    244            ?           0    0    stories_character_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.stories_character_id_seq', 1, false);
          public          postgres    false    251            ?           0    0    stories_objection_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.stories_objection_id_seq', 20, true);
          public          postgres    false    253            ?           0    0    stories_objectionhandle_id_seq    SEQUENCE SET     M   SELECT pg_catalog.setval('public.stories_objectionhandle_id_seq', 23, true);
          public          postgres    false    255            ?           0    0 *   stories_objectionhandlestatstracker_id_seq    SEQUENCE SET     Y   SELECT pg_catalog.setval('public.stories_objectionhandlestatstracker_id_seq', 1, false);
          public          postgres    false    265            ?           0    0 %   stories_objectioonstatstracker_id_seq    SEQUENCE SET     T   SELECT pg_catalog.setval('public.stories_objectioonstatstracker_id_seq', 1, false);
          public          postgres    false    263            ?           0    0    stories_story_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.stories_story_id_seq', 10, true);
          public          postgres    false    257            ?           0    0    stories_storycharacter_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.stories_storycharacter_id_seq', 1, false);
          public          postgres    false    261            ?           0    0     stories_storystatstracker_id_seq    SEQUENCE SET     O   SELECT pg_catalog.setval('public.stories_storystatstracker_id_seq', 1, false);
          public          postgres    false    259            +           2606    66074 Z   accounts_customuser_groups accounts_customuser_groups_customuser_id_group_id_c074bdcb_uniq 
   CONSTRAINT     ?   ALTER TABLE ONLY public.accounts_customuser_groups
    ADD CONSTRAINT accounts_customuser_groups_customuser_id_group_id_c074bdcb_uniq UNIQUE (customuser_id, group_id);
 ?   ALTER TABLE ONLY public.accounts_customuser_groups DROP CONSTRAINT accounts_customuser_groups_customuser_id_group_id_c074bdcb_uniq;
       public            postgres    false    222    222            .           2606    66064 :   accounts_customuser_groups accounts_customuser_groups_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.accounts_customuser_groups
    ADD CONSTRAINT accounts_customuser_groups_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.accounts_customuser_groups DROP CONSTRAINT accounts_customuser_groups_pkey;
       public            postgres    false    222            %           2606    66055 ,   accounts_customuser accounts_customuser_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.accounts_customuser
    ADD CONSTRAINT accounts_customuser_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.accounts_customuser DROP CONSTRAINT accounts_customuser_pkey;
       public            postgres    false    220            0           2606    66088 d   accounts_customuser_user_permissions accounts_customuser_user_customuser_id_permission_9632a709_uniq 
   CONSTRAINT     ?   ALTER TABLE ONLY public.accounts_customuser_user_permissions
    ADD CONSTRAINT accounts_customuser_user_customuser_id_permission_9632a709_uniq UNIQUE (customuser_id, permission_id);
 ?   ALTER TABLE ONLY public.accounts_customuser_user_permissions DROP CONSTRAINT accounts_customuser_user_customuser_id_permission_9632a709_uniq;
       public            postgres    false    224    224            4           2606    66071 N   accounts_customuser_user_permissions accounts_customuser_user_permissions_pkey 
   CONSTRAINT     ?   ALTER TABLE ONLY public.accounts_customuser_user_permissions
    ADD CONSTRAINT accounts_customuser_user_permissions_pkey PRIMARY KEY (id);
 x   ALTER TABLE ONLY public.accounts_customuser_user_permissions DROP CONSTRAINT accounts_customuser_user_permissions_pkey;
       public            postgres    false    224            (           2606    66057 4   accounts_customuser accounts_customuser_username_key 
   CONSTRAINT     s   ALTER TABLE ONLY public.accounts_customuser
    ADD CONSTRAINT accounts_customuser_username_key UNIQUE (username);
 ^   ALTER TABLE ONLY public.accounts_customuser DROP CONSTRAINT accounts_customuser_username_key;
       public            postgres    false    220                       2606    66045    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public            postgres    false    216                        2606    66031 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     ?   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public            postgres    false    218    218            #           2606    66020 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public            postgres    false    218                       2606    66011    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public            postgres    false    216                       2606    66022 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     ?   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public            postgres    false    214    214                       2606    66004 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public            postgres    false    214            ;           2606    66127 $   authtoken_token authtoken_token_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);
 N   ALTER TABLE ONLY public.authtoken_token DROP CONSTRAINT authtoken_token_pkey;
       public            postgres    false    227            =           2606    66129 +   authtoken_token authtoken_token_user_id_key 
   CONSTRAINT     i   ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);
 U   ALTER TABLE ONLY public.authtoken_token DROP CONSTRAINT authtoken_token_user_id_key;
       public            postgres    false    227            7           2606    66110 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public            postgres    false    226                       2606    65997 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     ?   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public            postgres    false    212    212                       2606    65995 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public            postgres    false    212                       2606    65988 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public            postgres    false    210            b           2606    66279 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public            postgres    false    248            f           2606    66290 ,   django_site django_site_domain_a2e37b91_uniq 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_domain_a2e37b91_uniq UNIQUE (domain);
 V   ALTER TABLE ONLY public.django_site DROP CONSTRAINT django_site_domain_a2e37b91_uniq;
       public            postgres    false    250            h           2606    66288    django_site django_site_pkey 
   CONSTRAINT     Z   ALTER TABLE ONLY public.django_site
    ADD CONSTRAINT django_site_pkey PRIMARY KEY (id);
 F   ALTER TABLE ONLY public.django_site DROP CONSTRAINT django_site_pkey;
       public            postgres    false    250            G           2606    66177 o   insuranceProducts_assessmentquestionnairemaster insuranceProducts_assessmentquestionnairemast_assessment_id_key 
   CONSTRAINT     ?   ALTER TABLE ONLY public."insuranceProducts_assessmentquestionnairemaster"
    ADD CONSTRAINT "insuranceProducts_assessmentquestionnairemast_assessment_id_key" UNIQUE (assessment_id);
 ?   ALTER TABLE ONLY public."insuranceProducts_assessmentquestionnairemaster" DROP CONSTRAINT "insuranceProducts_assessmentquestionnairemast_assessment_id_key";
       public            postgres    false    233            I           2606    66175 d   insuranceProducts_assessmentquestionnairemaster insuranceProducts_assessmentquestionnairemaster_pkey 
   CONSTRAINT     ?   ALTER TABLE ONLY public."insuranceProducts_assessmentquestionnairemaster"
    ADD CONSTRAINT "insuranceProducts_assessmentquestionnairemaster_pkey" PRIMARY KEY (id);
 ?   ALTER TABLE ONLY public."insuranceProducts_assessmentquestionnairemaster" DROP CONSTRAINT "insuranceProducts_assessmentquestionnairemaster_pkey";
       public            postgres    false    233            L           2606    66188 M   insuranceProducts_clientdetails insuranceProducts_clientdetails_client_id_key 
   CONSTRAINT     ?   ALTER TABLE ONLY public."insuranceProducts_clientdetails"
    ADD CONSTRAINT "insuranceProducts_clientdetails_client_id_key" UNIQUE (client_id);
 {   ALTER TABLE ONLY public."insuranceProducts_clientdetails" DROP CONSTRAINT "insuranceProducts_clientdetails_client_id_key";
       public            postgres    false    235            N           2606    66186 D   insuranceProducts_clientdetails insuranceProducts_clientdetails_pkey 
   CONSTRAINT     ?   ALTER TABLE ONLY public."insuranceProducts_clientdetails"
    ADD CONSTRAINT "insuranceProducts_clientdetails_pkey" PRIMARY KEY (id);
 r   ALTER TABLE ONLY public."insuranceProducts_clientdetails" DROP CONSTRAINT "insuranceProducts_clientdetails_pkey";
       public            postgres    false    235            D           2606    66154 P   insuranceProducts_insurancediscussion insuranceProducts_insurancediscussion_pkey 
   CONSTRAINT     ?   ALTER TABLE ONLY public."insuranceProducts_insurancediscussion"
    ADD CONSTRAINT "insuranceProducts_insurancediscussion_pkey" PRIMARY KEY (id);
 ~   ALTER TABLE ONLY public."insuranceProducts_insurancediscussion" DROP CONSTRAINT "insuranceProducts_insurancediscussion_pkey";
       public            postgres    false    231            U           2606    66208 `   insuranceProducts_insurancenoneligiblecontent insuranceProducts_insurancenoneligiblecontent_pkey 
   CONSTRAINT     ?   ALTER TABLE ONLY public."insuranceProducts_insurancenoneligiblecontent"
    ADD CONSTRAINT "insuranceProducts_insurancenoneligiblecontent_pkey" PRIMARY KEY (id);
 ?   ALTER TABLE ONLY public."insuranceProducts_insurancenoneligiblecontent" DROP CONSTRAINT "insuranceProducts_insurancenoneligiblecontent_pkey";
       public            postgres    false    239            W           2606    66217 X   insuranceProducts_insurancepreprocessdata insuranceProducts_insurancepreprocessdata_pkey 
   CONSTRAINT     ?   ALTER TABLE ONLY public."insuranceProducts_insurancepreprocessdata"
    ADD CONSTRAINT "insuranceProducts_insurancepreprocessdata_pkey" PRIMARY KEY (id);
 ?   ALTER TABLE ONLY public."insuranceProducts_insurancepreprocessdata" DROP CONSTRAINT "insuranceProducts_insurancepreprocessdata_pkey";
       public            postgres    false    241            @           2606    66142 J   insuranceProducts_insuranceproduct insuranceProducts_insuranceproduct_pkey 
   CONSTRAINT     ?   ALTER TABLE ONLY public."insuranceProducts_insuranceproduct"
    ADD CONSTRAINT "insuranceProducts_insuranceproduct_pkey" PRIMARY KEY (id);
 x   ALTER TABLE ONLY public."insuranceProducts_insuranceproduct" DROP CONSTRAINT "insuranceProducts_insuranceproduct_pkey";
       public            postgres    false    229            Q           2606    66199 K   insurance_credit_products insurance_credit_products_credit_product_code_key 
   CONSTRAINT     ?   ALTER TABLE ONLY public.insurance_credit_products
    ADD CONSTRAINT insurance_credit_products_credit_product_code_key UNIQUE (credit_product_code);
 u   ALTER TABLE ONLY public.insurance_credit_products DROP CONSTRAINT insurance_credit_products_credit_product_code_key;
       public            postgres    false    237            S           2606    66197 8   insurance_credit_products insurance_credit_products_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.insurance_credit_products
    ADD CONSTRAINT insurance_credit_products_pkey PRIMARY KEY (id);
 b   ALTER TABLE ONLY public.insurance_credit_products DROP CONSTRAINT insurance_credit_products_pkey;
       public            postgres    false    237            _           2606    66250 >   insurance_eligibility_master insurance_eligibility_master_pkey 
   CONSTRAINT     |   ALTER TABLE ONLY public.insurance_eligibility_master
    ADD CONSTRAINT insurance_eligibility_master_pkey PRIMARY KEY (id);
 h   ALTER TABLE ONLY public.insurance_eligibility_master DROP CONSTRAINT insurance_eligibility_master_pkey;
       public            postgres    false    247            Y           2606    66226 (   occupation_master occupation_master_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.occupation_master
    ADD CONSTRAINT occupation_master_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.occupation_master DROP CONSTRAINT occupation_master_pkey;
       public            postgres    false    243            [           2606    66235 8   province_residence_master province_residence_master_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.province_residence_master
    ADD CONSTRAINT province_residence_master_pkey PRIMARY KEY (id);
 b   ALTER TABLE ONLY public.province_residence_master DROP CONSTRAINT province_residence_master_pkey;
       public            postgres    false    245            k           2606    66302 5   stories_character stories_character_characterName_key 
   CONSTRAINT     }   ALTER TABLE ONLY public.stories_character
    ADD CONSTRAINT "stories_character_characterName_key" UNIQUE ("characterName");
 a   ALTER TABLE ONLY public.stories_character DROP CONSTRAINT "stories_character_characterName_key";
       public            postgres    false    252            m           2606    66300 (   stories_character stories_character_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.stories_character
    ADD CONSTRAINT stories_character_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.stories_character DROP CONSTRAINT stories_character_pkey;
       public            postgres    false    252            p           2606    66311 5   stories_objection stories_objection_objectionName_key 
   CONSTRAINT     }   ALTER TABLE ONLY public.stories_objection
    ADD CONSTRAINT "stories_objection_objectionName_key" UNIQUE ("objectionName");
 a   ALTER TABLE ONLY public.stories_objection DROP CONSTRAINT "stories_objection_objectionName_key";
       public            postgres    false    254            r           2606    66309 (   stories_objection stories_objection_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.stories_objection
    ADD CONSTRAINT stories_objection_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.stories_objection DROP CONSTRAINT stories_objection_pkey;
       public            postgres    false    254            u           2606    66320 >   stories_objectionhandle stories_objectionhandle_buttleName_key 
   CONSTRAINT     ?   ALTER TABLE ONLY public.stories_objectionhandle
    ADD CONSTRAINT "stories_objectionhandle_buttleName_key" UNIQUE ("buttleName");
 j   ALTER TABLE ONLY public.stories_objectionhandle DROP CONSTRAINT "stories_objectionhandle_buttleName_key";
       public            postgres    false    256            x           2606    66318 4   stories_objectionhandle stories_objectionhandle_pkey 
   CONSTRAINT     r   ALTER TABLE ONLY public.stories_objectionhandle
    ADD CONSTRAINT stories_objectionhandle_pkey PRIMARY KEY (id);
 ^   ALTER TABLE ONLY public.stories_objectionhandle DROP CONSTRAINT stories_objectionhandle_pkey;
       public            postgres    false    256            ?           2606    66360 L   stories_objectionhandlestatstracker stories_objectionhandlestatstracker_pkey 
   CONSTRAINT     ?   ALTER TABLE ONLY public.stories_objectionhandlestatstracker
    ADD CONSTRAINT stories_objectionhandlestatstracker_pkey PRIMARY KEY (id);
 v   ALTER TABLE ONLY public.stories_objectionhandlestatstracker DROP CONSTRAINT stories_objectionhandlestatstracker_pkey;
       public            postgres    false    266            ?           2606    66353 B   stories_objectioonstatstracker stories_objectioonstatstracker_pkey 
   CONSTRAINT     ?   ALTER TABLE ONLY public.stories_objectioonstatstracker
    ADD CONSTRAINT stories_objectioonstatstracker_pkey PRIMARY KEY (id);
 l   ALTER TABLE ONLY public.stories_objectioonstatstracker DROP CONSTRAINT stories_objectioonstatstracker_pkey;
       public            postgres    false    264            z           2606    66329     stories_story stories_story_pkey 
   CONSTRAINT     ^   ALTER TABLE ONLY public.stories_story
    ADD CONSTRAINT stories_story_pkey PRIMARY KEY (id);
 J   ALTER TABLE ONLY public.stories_story DROP CONSTRAINT stories_story_pkey;
       public            postgres    false    258            }           2606    66331 )   stories_story stories_story_storyName_key 
   CONSTRAINT     m   ALTER TABLE ONLY public.stories_story
    ADD CONSTRAINT "stories_story_storyName_key" UNIQUE ("storyName");
 U   ALTER TABLE ONLY public.stories_story DROP CONSTRAINT "stories_story_storyName_key";
       public            postgres    false    258            ?           2606    66346 2   stories_storycharacter stories_storycharacter_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.stories_storycharacter
    ADD CONSTRAINT stories_storycharacter_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.stories_storycharacter DROP CONSTRAINT stories_storycharacter_pkey;
       public            postgres    false    262            ?           2606    66338 8   stories_storystatstracker stories_storystatstracker_pkey 
   CONSTRAINT     v   ALTER TABLE ONLY public.stories_storystatstracker
    ADD CONSTRAINT stories_storystatstracker_pkey PRIMARY KEY (id);
 b   ALTER TABLE ONLY public.stories_storystatstracker DROP CONSTRAINT stories_storystatstracker_pkey;
       public            postgres    false    260            )           1259    66085 1   accounts_customuser_groups_customuser_id_bc55088e    INDEX     ?   CREATE INDEX accounts_customuser_groups_customuser_id_bc55088e ON public.accounts_customuser_groups USING btree (customuser_id);
 E   DROP INDEX public.accounts_customuser_groups_customuser_id_bc55088e;
       public            postgres    false    222            ,           1259    66086 ,   accounts_customuser_groups_group_id_86ba5f9e    INDEX     w   CREATE INDEX accounts_customuser_groups_group_id_86ba5f9e ON public.accounts_customuser_groups USING btree (group_id);
 @   DROP INDEX public.accounts_customuser_groups_group_id_86ba5f9e;
       public            postgres    false    222            1           1259    66099 ;   accounts_customuser_user_permissions_customuser_id_0deaefae    INDEX     ?   CREATE INDEX accounts_customuser_user_permissions_customuser_id_0deaefae ON public.accounts_customuser_user_permissions USING btree (customuser_id);
 O   DROP INDEX public.accounts_customuser_user_permissions_customuser_id_0deaefae;
       public            postgres    false    224            2           1259    66100 ;   accounts_customuser_user_permissions_permission_id_aea3d0e5    INDEX     ?   CREATE INDEX accounts_customuser_user_permissions_permission_id_aea3d0e5 ON public.accounts_customuser_user_permissions USING btree (permission_id);
 O   DROP INDEX public.accounts_customuser_user_permissions_permission_id_aea3d0e5;
       public            postgres    false    224            &           1259    66072 *   accounts_customuser_username_722f3555_like    INDEX     ?   CREATE INDEX accounts_customuser_username_722f3555_like ON public.accounts_customuser USING btree (username varchar_pattern_ops);
 >   DROP INDEX public.accounts_customuser_username_722f3555_like;
       public            postgres    false    220                       1259    66046    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public            postgres    false    216                       1259    66042 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public            postgres    false    218            !           1259    66043 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public            postgres    false    218                       1259    66028 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public            postgres    false    214            9           1259    66135 !   authtoken_token_key_10f0b77e_like    INDEX     p   CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);
 5   DROP INDEX public.authtoken_token_key_10f0b77e_like;
       public            postgres    false    227            5           1259    66121 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public            postgres    false    226            8           1259    66122 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public            postgres    false    226            `           1259    66281 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public            postgres    false    248            c           1259    66280 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public            postgres    false    248            d           1259    66291     django_site_domain_a2e37b91_like    INDEX     n   CREATE INDEX django_site_domain_a2e37b91_like ON public.django_site USING btree (domain varchar_pattern_ops);
 4   DROP INDEX public.django_site_domain_a2e37b91_like;
       public            postgres    false    250            E           1259    66257 4   insuranceProducts_assess_assessment_id_b984b710_like    INDEX     ?   CREATE INDEX "insuranceProducts_assess_assessment_id_b984b710_like" ON public."insuranceProducts_assessmentquestionnairemaster" USING btree (assessment_id varchar_pattern_ops);
 J   DROP INDEX public."insuranceProducts_assess_assessment_id_b984b710_like";
       public            postgres    false    233            J           1259    66258 7   insuranceProducts_clientdetails_client_id_0adbc48f_like    INDEX     ?   CREATE INDEX "insuranceProducts_clientdetails_client_id_0adbc48f_like" ON public."insuranceProducts_clientdetails" USING btree (client_id varchar_pattern_ops);
 M   DROP INDEX public."insuranceProducts_clientdetails_client_id_0adbc48f_like";
       public            postgres    false    235            >           1259    66272 9   insuranceProducts_insuranc_creditProduct_code_id_6143882b    INDEX     ?   CREATE INDEX "insuranceProducts_insuranc_creditProduct_code_id_6143882b" ON public."insuranceProducts_insuranceproduct" USING btree ("creditProduct_code_id");
 O   DROP INDEX public."insuranceProducts_insuranc_creditProduct_code_id_6143882b";
       public            postgres    false    229            A           1259    66165 7   insuranceProducts_insurancediscussion_agent_id_a7ab54fd    INDEX     ?   CREATE INDEX "insuranceProducts_insurancediscussion_agent_id_a7ab54fd" ON public."insuranceProducts_insurancediscussion" USING btree (agent_id);
 M   DROP INDEX public."insuranceProducts_insurancediscussion_agent_id_a7ab54fd";
       public            postgres    false    231            B           1259    66166 <   insuranceProducts_insurancediscussion_insProduct_id_3852148c    INDEX     ?   CREATE INDEX "insuranceProducts_insurancediscussion_insProduct_id_3852148c" ON public."insuranceProducts_insurancediscussion" USING btree ("insProduct_id");
 R   DROP INDEX public."insuranceProducts_insurancediscussion_insProduct_id_3852148c";
       public            postgres    false    231            O           1259    66259 ;   insurance_credit_products_credit_product_code_5636d2c2_like    INDEX     ?   CREATE INDEX insurance_credit_products_credit_product_code_5636d2c2_like ON public.insurance_credit_products USING btree (credit_product_code varchar_pattern_ops);
 O   DROP INDEX public.insurance_credit_products_credit_product_code_5636d2c2_like;
       public            postgres    false    237            \           1259    66270 3   insurance_eligibility_master_insProduct_id_be2c459b    INDEX     ?   CREATE INDEX "insurance_eligibility_master_insProduct_id_be2c459b" ON public.insurance_eligibility_master USING btree ("insProduct_id");
 I   DROP INDEX public."insurance_eligibility_master_insProduct_id_be2c459b";
       public            postgres    false    247            ]           1259    66271 3   insurance_eligibility_master_occupation_id_f9e47ec8    INDEX     ?   CREATE INDEX insurance_eligibility_master_occupation_id_f9e47ec8 ON public.insurance_eligibility_master USING btree (occupation_id);
 G   DROP INDEX public.insurance_eligibility_master_occupation_id_f9e47ec8;
       public            postgres    false    247            i           1259    66361 -   stories_character_characterName_2f229182_like    INDEX     ?   CREATE INDEX "stories_character_characterName_2f229182_like" ON public.stories_character USING btree ("characterName" varchar_pattern_ops);
 C   DROP INDEX public."stories_character_characterName_2f229182_like";
       public            postgres    false    252            n           1259    66362 -   stories_objection_objectionName_a1feb8e6_like    INDEX     ?   CREATE INDEX "stories_objection_objectionName_a1feb8e6_like" ON public.stories_objection USING btree ("objectionName" varchar_pattern_ops);
 C   DROP INDEX public."stories_objection_objectionName_a1feb8e6_like";
       public            postgres    false    254            s           1259    66368 0   stories_objectionhandle_buttleName_479c8032_like    INDEX     ?   CREATE INDEX "stories_objectionhandle_buttleName_479c8032_like" ON public.stories_objectionhandle USING btree ("buttleName" varchar_pattern_ops);
 F   DROP INDEX public."stories_objectionhandle_buttleName_479c8032_like";
       public            postgres    false    256            v           1259    66369 -   stories_objectionhandle_objection_id_1cdf160b    INDEX     y   CREATE INDEX stories_objectionhandle_objection_id_1cdf160b ON public.stories_objectionhandle USING btree (objection_id);
 A   DROP INDEX public.stories_objectionhandle_objection_id_1cdf160b;
       public            postgres    false    256            ?           1259    66435 :   stories_objectionhandlesta_insuranceDiscussion_id_7827ae11    INDEX     ?   CREATE INDEX "stories_objectionhandlesta_insuranceDiscussion_id_7827ae11" ON public.stories_objectionhandlestatstracker USING btree ("insuranceDiscussion_id");
 P   DROP INDEX public."stories_objectionhandlesta_insuranceDiscussion_id_7827ae11";
       public            postgres    false    266            ?           1259    66434 5   stories_objectionhandlestatstracker_agent_id_af2d10ad    INDEX     ?   CREATE INDEX stories_objectionhandlestatstracker_agent_id_af2d10ad ON public.stories_objectionhandlestatstracker USING btree (agent_id);
 I   DROP INDEX public.stories_objectionhandlestatstracker_agent_id_af2d10ad;
       public            postgres    false    266            ?           1259    66436 ?   stories_objectionhandlestatstracker_objectionHandle_id_160d8825    INDEX     ?   CREATE INDEX "stories_objectionhandlestatstracker_objectionHandle_id_160d8825" ON public.stories_objectionhandlestatstracker USING btree ("objectionHandle_id");
 U   DROP INDEX public."stories_objectionhandlestatstracker_objectionHandle_id_160d8825";
       public            postgres    false    266            ?           1259    66416 0   stories_objectioonstatstracker_agent_id_5e38f7d3    INDEX        CREATE INDEX stories_objectioonstatstracker_agent_id_5e38f7d3 ON public.stories_objectioonstatstracker USING btree (agent_id);
 D   DROP INDEX public.stories_objectioonstatstracker_agent_id_5e38f7d3;
       public            postgres    false    264            ?           1259    66417 >   stories_objectioonstatstracker_insuranceDiscussion_id_49edb9e8    INDEX     ?   CREATE INDEX "stories_objectioonstatstracker_insuranceDiscussion_id_49edb9e8" ON public.stories_objectioonstatstracker USING btree ("insuranceDiscussion_id");
 T   DROP INDEX public."stories_objectioonstatstracker_insuranceDiscussion_id_49edb9e8";
       public            postgres    false    264            ?           1259    66418 4   stories_objectioonstatstracker_objection_id_ad2bb58b    INDEX     ?   CREATE INDEX stories_objectioonstatstracker_objection_id_ad2bb58b ON public.stories_objectioonstatstracker USING btree (objection_id);
 H   DROP INDEX public.stories_objectioonstatstracker_objection_id_ad2bb58b;
       public            postgres    false    264            {           1259    66370 %   stories_story_storyName_afeff651_like    INDEX     |   CREATE INDEX "stories_story_storyName_afeff651_like" ON public.stories_story USING btree ("storyName" varchar_pattern_ops);
 ;   DROP INDEX public."stories_story_storyName_afeff651_like";
       public            postgres    false    258            ?           1259    66399 ,   stories_storycharacter_character_id_a589712f    INDEX     w   CREATE INDEX stories_storycharacter_character_id_a589712f ON public.stories_storycharacter USING btree (character_id);
 @   DROP INDEX public.stories_storycharacter_character_id_a589712f;
       public            postgres    false    262            ?           1259    66400 (   stories_storycharacter_story_id_f1a2fe18    INDEX     o   CREATE INDEX stories_storycharacter_story_id_f1a2fe18 ON public.stories_storycharacter USING btree (story_id);
 <   DROP INDEX public.stories_storycharacter_story_id_f1a2fe18;
       public            postgres    false    262            ~           1259    66386 +   stories_storystatstracker_agent_id_045c53db    INDEX     u   CREATE INDEX stories_storystatstracker_agent_id_045c53db ON public.stories_storystatstracker USING btree (agent_id);
 ?   DROP INDEX public.stories_storystatstracker_agent_id_045c53db;
       public            postgres    false    260                       1259    66387 9   stories_storystatstracker_insuranceDiscussion_id_61b2ed43    INDEX     ?   CREATE INDEX "stories_storystatstracker_insuranceDiscussion_id_61b2ed43" ON public.stories_storystatstracker USING btree ("insuranceDiscussion_id");
 O   DROP INDEX public."stories_storystatstracker_insuranceDiscussion_id_61b2ed43";
       public            postgres    false    260            ?           1259    66388 +   stories_storystatstracker_story_id_26d27312    INDEX     u   CREATE INDEX stories_storystatstracker_story_id_26d27312 ON public.stories_storystatstracker USING btree (story_id);
 ?   DROP INDEX public.stories_storystatstracker_story_id_26d27312;
       public            postgres    false    260            ?           2606    66089 ]   accounts_customuser_user_permissions accounts_customuser__customuser_id_0deaefae_fk_accounts_    FK CONSTRAINT     ?   ALTER TABLE ONLY public.accounts_customuser_user_permissions
    ADD CONSTRAINT accounts_customuser__customuser_id_0deaefae_fk_accounts_ FOREIGN KEY (customuser_id) REFERENCES public.accounts_customuser(id) DEFERRABLE INITIALLY DEFERRED;
 ?   ALTER TABLE ONLY public.accounts_customuser_user_permissions DROP CONSTRAINT accounts_customuser__customuser_id_0deaefae_fk_accounts_;
       public          postgres    false    224    3365    220            ?           2606    66075 S   accounts_customuser_groups accounts_customuser__customuser_id_bc55088e_fk_accounts_    FK CONSTRAINT     ?   ALTER TABLE ONLY public.accounts_customuser_groups
    ADD CONSTRAINT accounts_customuser__customuser_id_bc55088e_fk_accounts_ FOREIGN KEY (customuser_id) REFERENCES public.accounts_customuser(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.accounts_customuser_groups DROP CONSTRAINT accounts_customuser__customuser_id_bc55088e_fk_accounts_;
       public          postgres    false    220    222    3365            ?           2606    66094 ]   accounts_customuser_user_permissions accounts_customuser__permission_id_aea3d0e5_fk_auth_perm    FK CONSTRAINT     ?   ALTER TABLE ONLY public.accounts_customuser_user_permissions
    ADD CONSTRAINT accounts_customuser__permission_id_aea3d0e5_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 ?   ALTER TABLE ONLY public.accounts_customuser_user_permissions DROP CONSTRAINT accounts_customuser__permission_id_aea3d0e5_fk_auth_perm;
       public          postgres    false    224    214    3352            ?           2606    66080 X   accounts_customuser_groups accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.accounts_customuser_groups
    ADD CONSTRAINT accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 ?   ALTER TABLE ONLY public.accounts_customuser_groups DROP CONSTRAINT accounts_customuser_groups_group_id_86ba5f9e_fk_auth_group_id;
       public          postgres    false    216    3357    222            ?           2606    66037 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public          postgres    false    218    3352    214            ?           2606    66032 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public          postgres    false    218    216    3357            ?           2606    66023 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     ?   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public          postgres    false    214    212    3347            ?           2606    66130 J   authtoken_token authtoken_token_user_id_35299eff_fk_accounts_customuser_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_accounts_customuser_id FOREIGN KEY (user_id) REFERENCES public.accounts_customuser(id) DEFERRABLE INITIALLY DEFERRED;
 t   ALTER TABLE ONLY public.authtoken_token DROP CONSTRAINT authtoken_token_user_id_35299eff_fk_accounts_customuser_id;
       public          postgres    false    3365    227    220            ?           2606    66111 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     ?   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public          postgres    false    226    212    3347            ?           2606    66116 L   django_admin_log django_admin_log_user_id_c564eba6_fk_accounts_customuser_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_accounts_customuser_id FOREIGN KEY (user_id) REFERENCES public.accounts_customuser(id) DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_accounts_customuser_id;
       public          postgres    false    226    3365    220            ?           2606    66155 Y   insuranceProducts_insurancediscussion insuranceProducts_in_agent_id_a7ab54fd_fk_accounts_    FK CONSTRAINT     ?   ALTER TABLE ONLY public."insuranceProducts_insurancediscussion"
    ADD CONSTRAINT "insuranceProducts_in_agent_id_a7ab54fd_fk_accounts_" FOREIGN KEY (agent_id) REFERENCES public.accounts_customuser(id) DEFERRABLE INITIALLY DEFERRED;
 ?   ALTER TABLE ONLY public."insuranceProducts_insurancediscussion" DROP CONSTRAINT "insuranceProducts_in_agent_id_a7ab54fd_fk_accounts_";
       public          postgres    false    220    231    3365            ?           2606    66252 b   insuranceProducts_insuranceproduct insuranceProducts_in_creditProduct_code_i_6143882b_fk_insurance    FK CONSTRAINT       ALTER TABLE ONLY public."insuranceProducts_insuranceproduct"
    ADD CONSTRAINT "insuranceProducts_in_creditProduct_code_i_6143882b_fk_insurance" FOREIGN KEY ("creditProduct_code_id") REFERENCES public.insurance_credit_products(id) DEFERRABLE INITIALLY DEFERRED;
 ?   ALTER TABLE ONLY public."insuranceProducts_insuranceproduct" DROP CONSTRAINT "insuranceProducts_in_creditProduct_code_i_6143882b_fk_insurance";
       public          postgres    false    237    229    3411            ?           2606    66160 ^   insuranceProducts_insurancediscussion insuranceProducts_in_insProduct_id_3852148c_fk_insurance    FK CONSTRAINT       ALTER TABLE ONLY public."insuranceProducts_insurancediscussion"
    ADD CONSTRAINT "insuranceProducts_in_insProduct_id_3852148c_fk_insurance" FOREIGN KEY ("insProduct_id") REFERENCES public."insuranceProducts_insuranceproduct"(id) DEFERRABLE INITIALLY DEFERRED;
 ?   ALTER TABLE ONLY public."insuranceProducts_insurancediscussion" DROP CONSTRAINT "insuranceProducts_in_insProduct_id_3852148c_fk_insurance";
       public          postgres    false    231    3392    229            ?           2606    66260 U   insurance_eligibility_master insurance_eligibilit_insProduct_id_be2c459b_fk_insurance    FK CONSTRAINT     ?   ALTER TABLE ONLY public.insurance_eligibility_master
    ADD CONSTRAINT "insurance_eligibilit_insProduct_id_be2c459b_fk_insurance" FOREIGN KEY ("insProduct_id") REFERENCES public."insuranceProducts_insuranceproduct"(id) DEFERRABLE INITIALLY DEFERRED;
 ?   ALTER TABLE ONLY public.insurance_eligibility_master DROP CONSTRAINT "insurance_eligibilit_insProduct_id_be2c459b_fk_insurance";
       public          postgres    false    3392    229    247            ?           2606    66265 U   insurance_eligibility_master insurance_eligibilit_occupation_id_f9e47ec8_fk_occupatio    FK CONSTRAINT     ?   ALTER TABLE ONLY public.insurance_eligibility_master
    ADD CONSTRAINT insurance_eligibilit_occupation_id_f9e47ec8_fk_occupatio FOREIGN KEY (occupation_id) REFERENCES public.occupation_master(id) DEFERRABLE INITIALLY DEFERRED;
    ALTER TABLE ONLY public.insurance_eligibility_master DROP CONSTRAINT insurance_eligibilit_occupation_id_f9e47ec8_fk_occupatio;
       public          postgres    false    243    3417    247            ?           2606    66419 W   stories_objectionhandlestatstracker stories_objectionhan_agent_id_af2d10ad_fk_accounts_    FK CONSTRAINT     ?   ALTER TABLE ONLY public.stories_objectionhandlestatstracker
    ADD CONSTRAINT stories_objectionhan_agent_id_af2d10ad_fk_accounts_ FOREIGN KEY (agent_id) REFERENCES public.accounts_customuser(id) DEFERRABLE INITIALLY DEFERRED;
 ?   ALTER TABLE ONLY public.stories_objectionhandlestatstracker DROP CONSTRAINT stories_objectionhan_agent_id_af2d10ad_fk_accounts_;
       public          postgres    false    3365    220    266            ?           2606    66424 c   stories_objectionhandlestatstracker stories_objectionhan_insuranceDiscussion__7827ae11_fk_insurance    FK CONSTRAINT       ALTER TABLE ONLY public.stories_objectionhandlestatstracker
    ADD CONSTRAINT "stories_objectionhan_insuranceDiscussion__7827ae11_fk_insurance" FOREIGN KEY ("insuranceDiscussion_id") REFERENCES public."insuranceProducts_insurancediscussion"(id) DEFERRABLE INITIALLY DEFERRED;
 ?   ALTER TABLE ONLY public.stories_objectionhandlestatstracker DROP CONSTRAINT "stories_objectionhan_insuranceDiscussion__7827ae11_fk_insurance";
       public          postgres    false    3396    266    231            ?           2606    66429 a   stories_objectionhandlestatstracker stories_objectionhan_objectionHandle_id_160d8825_fk_stories_o    FK CONSTRAINT     ?   ALTER TABLE ONLY public.stories_objectionhandlestatstracker
    ADD CONSTRAINT "stories_objectionhan_objectionHandle_id_160d8825_fk_stories_o" FOREIGN KEY ("objectionHandle_id") REFERENCES public.stories_objectionhandle(id) DEFERRABLE INITIALLY DEFERRED;
 ?   ALTER TABLE ONLY public.stories_objectionhandlestatstracker DROP CONSTRAINT "stories_objectionhan_objectionHandle_id_160d8825_fk_stories_o";
       public          postgres    false    256    266    3448            ?           2606    66363 O   stories_objectionhandle stories_objectionhan_objection_id_1cdf160b_fk_stories_o    FK CONSTRAINT     ?   ALTER TABLE ONLY public.stories_objectionhandle
    ADD CONSTRAINT stories_objectionhan_objection_id_1cdf160b_fk_stories_o FOREIGN KEY (objection_id) REFERENCES public.stories_objection(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.stories_objectionhandle DROP CONSTRAINT stories_objectionhan_objection_id_1cdf160b_fk_stories_o;
       public          postgres    false    254    256    3442            ?           2606    66401 R   stories_objectioonstatstracker stories_objectioonst_agent_id_5e38f7d3_fk_accounts_    FK CONSTRAINT     ?   ALTER TABLE ONLY public.stories_objectioonstatstracker
    ADD CONSTRAINT stories_objectioonst_agent_id_5e38f7d3_fk_accounts_ FOREIGN KEY (agent_id) REFERENCES public.accounts_customuser(id) DEFERRABLE INITIALLY DEFERRED;
 |   ALTER TABLE ONLY public.stories_objectioonstatstracker DROP CONSTRAINT stories_objectioonst_agent_id_5e38f7d3_fk_accounts_;
       public          postgres    false    220    3365    264            ?           2606    66406 ^   stories_objectioonstatstracker stories_objectioonst_insuranceDiscussion__49edb9e8_fk_insurance    FK CONSTRAINT       ALTER TABLE ONLY public.stories_objectioonstatstracker
    ADD CONSTRAINT "stories_objectioonst_insuranceDiscussion__49edb9e8_fk_insurance" FOREIGN KEY ("insuranceDiscussion_id") REFERENCES public."insuranceProducts_insurancediscussion"(id) DEFERRABLE INITIALLY DEFERRED;
 ?   ALTER TABLE ONLY public.stories_objectioonstatstracker DROP CONSTRAINT "stories_objectioonst_insuranceDiscussion__49edb9e8_fk_insurance";
       public          postgres    false    231    3396    264            ?           2606    66411 V   stories_objectioonstatstracker stories_objectioonst_objection_id_ad2bb58b_fk_stories_o    FK CONSTRAINT     ?   ALTER TABLE ONLY public.stories_objectioonstatstracker
    ADD CONSTRAINT stories_objectioonst_objection_id_ad2bb58b_fk_stories_o FOREIGN KEY (objection_id) REFERENCES public.stories_objection(id) DEFERRABLE INITIALLY DEFERRED;
 ?   ALTER TABLE ONLY public.stories_objectioonstatstracker DROP CONSTRAINT stories_objectioonst_objection_id_ad2bb58b_fk_stories_o;
       public          postgres    false    254    264    3442            ?           2606    66389 N   stories_storycharacter stories_storycharact_character_id_a589712f_fk_stories_c    FK CONSTRAINT     ?   ALTER TABLE ONLY public.stories_storycharacter
    ADD CONSTRAINT stories_storycharact_character_id_a589712f_fk_stories_c FOREIGN KEY (character_id) REFERENCES public.stories_character(id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.stories_storycharacter DROP CONSTRAINT stories_storycharact_character_id_a589712f_fk_stories_c;
       public          postgres    false    262    252    3437            ?           2606    66394 S   stories_storycharacter stories_storycharacter_story_id_f1a2fe18_fk_stories_story_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.stories_storycharacter
    ADD CONSTRAINT stories_storycharacter_story_id_f1a2fe18_fk_stories_story_id FOREIGN KEY (story_id) REFERENCES public.stories_story(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.stories_storycharacter DROP CONSTRAINT stories_storycharacter_story_id_f1a2fe18_fk_stories_story_id;
       public          postgres    false    262    3450    258            ?           2606    66371 M   stories_storystatstracker stories_storystatstr_agent_id_045c53db_fk_accounts_    FK CONSTRAINT     ?   ALTER TABLE ONLY public.stories_storystatstracker
    ADD CONSTRAINT stories_storystatstr_agent_id_045c53db_fk_accounts_ FOREIGN KEY (agent_id) REFERENCES public.accounts_customuser(id) DEFERRABLE INITIALLY DEFERRED;
 w   ALTER TABLE ONLY public.stories_storystatstracker DROP CONSTRAINT stories_storystatstr_agent_id_045c53db_fk_accounts_;
       public          postgres    false    220    3365    260            ?           2606    66376 Y   stories_storystatstracker stories_storystatstr_insuranceDiscussion__61b2ed43_fk_insurance    FK CONSTRAINT       ALTER TABLE ONLY public.stories_storystatstracker
    ADD CONSTRAINT "stories_storystatstr_insuranceDiscussion__61b2ed43_fk_insurance" FOREIGN KEY ("insuranceDiscussion_id") REFERENCES public."insuranceProducts_insurancediscussion"(id) DEFERRABLE INITIALLY DEFERRED;
 ?   ALTER TABLE ONLY public.stories_storystatstracker DROP CONSTRAINT "stories_storystatstr_insuranceDiscussion__61b2ed43_fk_insurance";
       public          postgres    false    3396    231    260            ?           2606    66381 Y   stories_storystatstracker stories_storystatstracker_story_id_26d27312_fk_stories_story_id    FK CONSTRAINT     ?   ALTER TABLE ONLY public.stories_storystatstracker
    ADD CONSTRAINT stories_storystatstracker_story_id_26d27312_fk_stories_story_id FOREIGN KEY (story_id) REFERENCES public.stories_story(id) DEFERRABLE INITIALLY DEFERRED;
 ?   ALTER TABLE ONLY public.stories_storystatstracker DROP CONSTRAINT stories_storystatstracker_story_id_26d27312_fk_stories_story_id;
       public          postgres    false    260    258    3450            B     x?m?QO?0???_?????ڮ[b? ?`?
?????m0p?s~?3ȋr?IN???*?&~??Sfc???=?j?1???e:!??L	[??Y??hO????????;&{??rH??/G2?n ??!k#x?P@X@]?a?s?i?B??H?|?I;?rDո?O????1???????I????L?f?*???z?C;2?G<X????)?Ӭ?,`)???r??y???-?????A?L???8???,J??TI?TY?;&5???Ņ"??6xs,??t?i      D      x?3?4?4?????? ?Y      F      x?????? ? ?      >   ,   x?3?tt	???2?t?trvt????2??C\? ?1z\\\ ??
=      @      x?????? ? ?      <   ?  x??X˒?6<_?/H-??s~??T?h
?a?%??? ??puq?Dw??݀\?S??n?s?KQ????s?????????O??kqO?X?M??PZ??9?_???S?f????O?.?|{[Q???{z?:^?Ģj3???,???x?mH4?SF?
????????T4?\\Q՛? ??9???~?*??R??Ǝ9?	]?????CO[??S??Y??q??G?nf/?v  ?QU?G?Z???B????Z?F?B??C{-i??B?&9??]릷~????9־?w???Ae?_?\?2?w3p???f?p?F|%?`X̖ق?:t?[?.?k??Fj?D??=?ɤ?HdZ???#??o??R?????????fFX?q.?!?P?Aȥ#?2?@1???(???NR?R???4???[???%=84-﫪9?WA&?IP? i??hA%1s???A????0<?*>u?v(?=?L+?h9rTbR?9???ĳM欘?????>?E??M?O?95???JXPD?̤2d?L?.sr??R??F????
?}?>?????T{??	??? q???D??ABL?D 73?cJ?B?~?7F?.???j!? ?O???d???"?e ?	q1?????a߬E?nv??:A? ?[+b!Q ???,3 ??qM^ei???n?`?ź??Ԋ%3VZ?'???1m?;?FÞ<)&??A??=??F?A???@??0T??t??a???
?0???Znf??طMk?+???:?/??j??d??l??ۤ??;D?)???;?&麼M?????4??]?ƀ?b???f?%???O?	fr.?$?IuD?K:??R!$0U?q???U??2Or=9]P?ˤ?%??A?/2(?	?b:????\_Mt???b^?gu??!B!? J???E m??롗???????"?QH*???CC2!?ߕ?%b???!c??/??Q??>`?b& ?<?@?E aK???????>??ݱO??W?
???????)?_S8?=???
GG???`???zTW?)???8???L?8f(?r!?1?%??? ????
? ??0????Z?zc?[?D/ln??u?+??O???#??k?H??.?Q??7???Qk>?E<ai?g??)A??? ??$???????PJ?(??=      I      x?????? ? ?      H   ?   x?}νn?0??y
?+??????ZEꟈ?qJ?*C?x?J?*?n????
Į?]?Ja?p%uG(?7??ӨI?sy?sf?n??D???????@?Oo???C?xI??%?D#UrR⣒?<G??m
,h.䵖?{??Ç?4?jڊ?k????a?p??/??_塉v[V????슲{??׮\??s?C8??????~W?m??}o??(?>2?h?      :   =  x?}RKv? \????????%jlp??kn_9NҺq??0?43ȕ?R?*.????q??1zͩ.??H7 ??#?,?O8EXM?P?DZ??QH?h9S??&????&En6s?!???mn??1Ej?ȇ?B?j
???????FE?OpS??>?-M??`Y?O6 ?pM????\r?z??;?Tf?W9a?pUY>?tx???j??0֍ɭW?׺nƀ(??u??ݷ??_??'?ǵ??L?h~??n9?&m??W??\G???_?~??9???ݦ?????x?N?"?o???՚??u???d?L???qm?? ??,7      8   ?  x????n?0??????U?g|?S??d??M??r?ڷ?!?Qܖ??1???*t???????c\??c]6;d?OL=?p {????2y?l???z߆7??n~⺲?y?B!?B??r_?OA1??,A"?+????????:t?ﺶ|w??N?V?܊??L4?Ц?.?-??[炩?H?A???T8?C?"?@?Pt??5?)??5?TS?S?I??6?.?8???:?}?ernn_????k?0zI??l?c9?~p???|߇޵~ʓ??>F???&ۦoZ??	f???FR??0Ҁ-?S??6??,????t?vyw????J??^i#??Z??t?uy?u??>C?FB??0u??[)?Mը?ȘJ5chgQkL?B߱?f?c?,?(M ?ۺ???%Jk?Ѧ`oa8[???F????`ZBT???8?'?j?W?sS?\?????+c???1??JB?C??P??A?(
U??y?1?F???.??棭?"jŮ/?????q????! ?Ɓ??#R9?L?5h??4(P???j7??i??!??D?????q??B˔???E??"????u?	?
1-[?;?A_o???1?lv?0	????>h??8>kw??_U?0????/?0iYq\?zfT
??gX???Eo?;+??c?y??J??$?_
?f?;??n0?gh????r???c9?aAǸJ)\??Q?,??dII32??a?????!#?w?????̟x      ^     x???n?@ е|E?f悼v?
ꀈE҄T? ??o??\?1?@?Nw?U???7<qE?A?,???:նM???l?姜˔h)7?]\??/$?p?Ko2???(??T?vmH??#Ii?S ?Qi???:??{?????v.??^2???8??]?9̍JP89???m?"?p?Ρ?`
?ѩ?ޫ-"Y^X??R????Ggws?φ({9<?|<???3?f4<???v???3??^ ?"????!k?????????????R??]?      `      x?3?L?H?-?I?K??Efs??qqq ?[	?      O   ?  x???ˎ?0???S?]U,_??7?MW]??<?
?̤y??@UBF]f*??8??O?1dC1?{,???9?y?!)?$??9ß?߇?l~?Ɵ?zx-t?i??B,MD /?*w??nĺP[0E???T????0????{?ܶiЁ??&???.^??U3.gmuH?!?wWX???>???x4??{L?P?=?{F6qK??B?0??5s`4@?? ?9!?K??o`W?ؓȖ)GD
?Ś?90Ȟ? _d
I?$?k??h??????9Ϩ???`??C/???)???|$e??埭??u??&???|?h???r??#QW?w~xq??f?<??	F?)??Y?G/??yQ????*V??P*n?N??f??^&??LQ???\M5?Q??i'`j???%??i?v`?k??/x?i6?Hۍ1뻾?㴃?C???vpN?+????4?*??E???n?a?>??K?%?q"3*'?JqN??[???ܽ??v??"7c      Q      x?????? ? ?      M      x?????? ? ?      U   ?   x?E??n?@E??+???#????6?l&`?%2F3????T???-?룫OFS???
Z??Ҟm???/o?n??4?i?m?????8?_??u̕?a??>?@??vY??9I ???;?x??#? ?ҥw??њ???\?r?_F?^????g??̳??xN;y	?-?ʴW =9&?ߘ??8?p??#???????T??S:?MSj???Rq?????WV?      W   ?  x??W?s?8~N?
&??r??t??mڤ?>57!-?9[?Ir??????2?&????x ???iw?i??????_???G:?7??#??H0?_??( ??0 ???c????Ȑ?;⚮??ɏ???9??????z??Cc0??YqM?va? ?????
;M?X0j???̒e???	????y???vqj?%???yqIcYZ?f?װ??N$??FH?#8??C??8?&V???Yc?[???? ,iL?J?OH9??De?dk???5??\???/$T?5?*??
K???Us?o??͆?>֦??*K?E?X??\ڍc?!?d???E????gz?;?1c??LsX??
	T??z? ?3?????$????Ѝ?%S?؏4??k?R??7Gܦ l?H???????;???솸m???L?f???d(?ҜEx:c?o?????W@m?tjөл??I??9???ch???_`%???
??cƝ????
Tgy??<ԝ~+?Ń|K??R&?l?ډ??^???2?|?&???~/????F9?ʘ?D??+b??"!v?ܽ?5???y:e?*ݙI??j??4??,??74?dYf?m?2?x??iعo[?ne{O?EME+??칒?	?~??iu?%h?#J????e?9"}_?i??8X???{??阪+?+ةj/Z4{??Lfo&?x??WI1??_h?|q?P?Q??rf??̴F@??pp?W?\@o%Z?*)??{r????Qd???????O??<?u|??Q???[e??x?ҭ9?̦ąa?1???lλq(??????U?m͝5?^%e-?^u??4??VS??߁/T̛?bu[^/o@?8F?3楬&??X???Ik???ܖ??ɱ??F??%^8?><> ??i???=?????c;>??c;>????d????9Zݎ???؎????????y=?      K   |  x????n?0??y
/??j??|a?t?*3???????.??5?H!?NGbǑ??7`?????)???@o??dO??K?JG?"????6??P???????k?w?立??Տó>Ӥ???;]???~??8??q?5???˳?O?YPX ]?s%;#l?\:)~D??t!?n#?"?V?`?	rrd?5???C??\!i!ᒔR|?i
?-K???6?????ʊ?[??0?sYXҒ`??l????$2^???92???ϵt?Zd?{????Y?????J????i??g?% kP???˦o?q?p?Ł?Ou????X&?g8????????????f?????2??֗@?"`4????{8E?????>??(> ??
?      S   ?   x??ν
?0?9y
?b??I?ЂЖ]?K%???T'?Z
w?p??!E@T?-??hmd0????????Ηj R)??vԨy??M?ʫ?"?:??T?s~N?|Um?ەA??V?[???&???õ*RD??nTT????{Ltc???'JA      ]   ?   x??ӽj1???)???K?,y??'??ܩ?O(M??	x?`???r??6?l2???????@x?????????~???~??}???k???????G??M??L56ny??2??d?s2?f??W???/M)?w&rhWD???F?"'?D?v4Ūt??3?	I?g??e???J??9%??\?D;?D݋1?Zd?iF?"?Eʑ???@L??`?/?'k?r|z?؃}X?/?lIPY????X/?J??? ??ɝ      Y   ?   x??α
?0??????!w??1???O?E?C?)D?oo?[Kn???I?H??N??qXx?CR???n?G?K???P5??i??1??`uE=Ӹ̏Wmv?u???gV?×??J́?????|?<Yc??8?      [   ?   x?u??
?0E??+ܗ??LF???k??nb[h?U????
??>`??s???x??*t`kIZg9??? ? H?#+??z??yI?0w??WQ?.????nKE?%???I???m???
]??&????W,? A?S?? ?6?Z???R?!Nq??e?η&?e?g?8??S??3V???nW^ms?7?A&Irj\X4      b      x?????? ? ?      d   ?  x??V?n?6=;_?S/E??,Y??????.??J?DDdR ???????_?P?l??? ??=??*??,?Y??r¢"q????_YZl?;hIx??7'??7 ?z?_`?9??V?KK?J?ҍ?????QF?<k?P??? ?4?5?_H????c?h?A?w?p?,?U?v)hS?VJ???????H91??N
?%G?,_Up?~?9???>??HS????--????{?F?A??ķ?2??`????hi?u?='?ux21e~??`??,<?>Z?O???y?x?@??&?u?9Zb???bf??&?p???s?C??
????ȥ???x?Jx??????ݧ???"?v? ??????iUO8&??Yi?Iߑ?Z???H?UR䓢r?daE????Yle???#۠g???ƍ?k^[d2???&?	8`ƮT?	@?	y?J~??t?l??7??WW?F?z0殞??oW?;ʢP#??w#????:?/7???1jи]?jn?7??p	??y00ep"{~"??y</?H*??:?ܽV?Pϴo???9M??????o????0}ڞV??%~?4?W??C????ӤAZ???葟nN?????/CT?H?u???Q?@?<?K???iN}U?"?I??K??^]?¶??
?????Jp?㸕?k1??=??????G?n?&?]?D?O?????/O??44??5??lK:5? 2?mu?:#Z??sӘ?*vNE?b
???+????e^׸D,v?n??@Z焙ċ?'???}W^M???3??/e_Č?8,4fҕ??,???y??J??d?"I)~?-???K[????"*?	?qqL????z3??y????V?;jv?1ca???g?q?A?*?\?
@?f??5?	tD??V???'}xx??<?      f   ?	  x??Yێ??}???_?H-?:?c3???X^??Ȧ??-??#+????9U?MR?],6?`?а?u?Tթv<?????lu7??x?\n?Y4???q??.f?1?xPɳ?t-L?ey??ʊT???F???YU??R*5"?/??<q?M-???ؼڋ?2M-?D	U?fV??no&???g!32Y???????yY?4?V??羙?j?X[?I<??;??j>?j??m???b??????1Od!Ty,??)?L??иc?D?<N>??%OU*??f?îF??8?q???+L? ??Mea????????Y???C0???Ot?????uS?n??o ?????v5?˛?_??9 ??F??????????M???v4{???`??:?8????j?K??&4?*ѥ?W?>????n3????I??]??RV??Sn?PƄń~?J?_}=?ʨ>hs?r?f??b}#B????*?`?<????g?*??˼??ɓx???m02w????v*???+<H?]0??1?É??S?????????M??H%?u?Dp?V???']?????r+>}????9??2??U?^$\? ?ƶ?Fg??)?8?D쑶T?,>??w`?1????$un9?gEnd?w?Zxo???on?????"??áĶ6??	B?¥&???????(????d?SHu{D±;?u???`}3???Ǒ??Kؒ<?((Tf?????Ao???HV??j?V??????I??A??&?e?گ?F?@?L+?8?@??	 ??i85[?p?#TF?څ1|¶??t?l/bWޤ?????lŋ&F߻s??
?j/x?Bk??t?`??Z???H?^%d??ta?N.? )y?%[A?'?NG?D?pQ{??#???ϡo???e???mNa8j?oPx?(??O?:???k}"????<?8?????p ??芛ix??*ܔc?O?VwNZ{'?ݰ????!^?;i0???;F??,?Z??y????Ome??ʵ?????J???Lo<4C??N݀f0?.??????ي;eB??y??"?'???
?'O=9O!1???^ H???abs*?kY?7???6??u??_Ӥ????P+܄pcēH????ge9?HJY}?{_<???!??o??`??9???h????	l??! ??*ڬ??pF?$䋂??tQ?O??'?*_???>͐?Ryf?l?
9?"?B????Ԃ?=?jG???bp?$?j??Q? 4????C?v?????=(?o?e???q?z???gN?8???1M	??'O?yPy???,?́j?!??TDJ?Է9???????q??G???rZ?5/????z???s4b?bh[?]???-??#n0O???T????4?F???????ˡYKX?b?0n?`?)i????U(?эX??#ů?E
Ii?2(4?ՖsE?n???z"Y;?k?6]+??αta????R:v?d*~????$??????eǫ?u???"Z?cR?z??sR???ׂ?.(???$??`?s:((?Z<>???????⚽???u?????3 ?F?P?-4o?-g??3?|?{??ipUvJ?H?f}??????Y<'1FJ?0?5???崹?'t??=7??2^Ϩ?/?c??zt,.z?˫_1(]^q)8??8?ƨ_?A?Ǜ????|?F[???'N?>?޿{d????q?±??i?OL?:?:8?"t?????f??	8P5?D?S[??	?)Nj?2oJ???R?d??L*N?K(?o\??a-mť????<G??AQ?4eS8u.IS?K?;y
q?>??d???0DE	.????X d?C??>@[/oz?b??C???GI???To?o?1B?ԕ=?^?8t?rJ??=?Ȼ??r	/t]??:y????C??~?`?;?п?D?}AR?$h觋??B[?}y??67<5? 3?DY)?	?z???#???^i?l??j??d&-Ȩ??B??S??}JG?<A??#~ܩ?l?w	???:??????????W?'? ?w~?f;_B?????ѷ
W@???o?0N????j??6ȽF??ǅ???/
)?$?ٝ?????X?????P?$,:???bs??<lic??7c0???1??w??Q?N18?F?:5??{??y????Fߚ<o?????[??W?d^?N?%U?,???a?$6?G_??G?*?|??i?*?}??Л??u,oky?ߥ?؃??n??~??a^?_?o??f?#???IYn?)?P??S?S,p??ܦ?6b??j?p?_7?^$??]??7X[?w?C??v_??_]*z??sQhs??6g??Ff9????=I?6dq?p?JQe?mK&?y???)???E?4?t??b???g?rǺ??Ҁ,?m????????er???.P?????e:=:ыy?
A?@P?moΥW-聬)ؑ??]???j??XN(??t?cx?????%?b?D?^??x|?V      p      x?????? ? ?      n      x?????? ? ?      h   z  x??X?n?6??>?7l??&Fo??i?E??bQ?74EI?Ф*R???>|??W虡d?Z?e?ȯIgΜ93?j?^?W?????V,׻???f?ݮ?^.???埬~?????G?J?c???NZ?>?Z|?c??^?@[>t~1l???o??ۍ8j?osqH??B?΋X?(*D??v??^k'r???s!].L?w?S[???7:???7?D????'???JD?.(?h>Q<?<??m?s????1[?i??^H???Ŷq?8^??;8????5???(J/??????֤R)ߺ?E܅o`?ɘ??|?V?J??X;?-??]	8C?k<W'?2xPtSj???h?#&??Mmk?F?'?̥??<?/?s?] :??m????
N???g)p??G?A?\???쁊?H??yn?pF?B[׾???[??DJ?ֻ????&??붆+??g?3??љAtX????l?K[??Rh?E??2 ?	??d?(?ZK?<8?;
k???ùקT(_?+ަƨ!E?R?p?Z ?iU1?NwHTm?? O"~2i??I??>0??W?;?d????Q?????9N?ǆ??????\???T2?*? 6?=@˯??????_Hn`?q?t????????b?,w?e???^ԓ?*?????Dp????G???\??n?>4:??U??J??IX?,u??t?@?b?h=??3L?O?q?ra??\?;'
?#;v2P?'}???;«H??V?????P,?ZwI?H?`&?սȥ??%ȏI??Y?{~T?dù??)?X????f@BF~9V?>?c/n&q????ω{??E?d????????j?Zo?@?$?xϨ?,??7?Rsu?{??H?!cRo?U?Q"Z??u?e?
D?Aw?<Ae??f"ih$??EzL??ηe5???? ???o??
S??C??d?ʗe?	??J(??1?[????`??Z ??<?\?y?2c򝊖5Y?,HB?H??dc<???z)S????5?q2Hr???G??֑?+"cR}:g?H?c]<Ee	
I?}?	??????????j???6ۛ??[???D???%??p?@???E?~????ISDL"?^?G??hc?w~???6IG?=Y??c??/?Qw)?ȏXuL4??P,?D,?l???A????8?5Q????V?5??@?E???C?????PbPT?k????_C?1d?<?????>&l3O	}e???r?f?c?ޥv??;4/G??H??XԚoyF2*9~?#??v?f?Ze??.?????wI?^K?MN?;??X? ??W?P???o¹n1;?!??<??>????PqB?h1??4e\c??	?W_???f??3}?JQ??0?~??Նu?ƹ?Ъ?,.??%??OG?a??O݉hQ???'T?9I?SG.?:z??xNO????[?6d??9?@?.[?<????X???`??I???[>??r???Ȏ?m??#l?kiN???Jg$?aIFߌ?~8?Wu?u???t	w???PK?;b_?{S?4??ڨ]?&?$?0K??)??D?s??ڭ????e?V?D???????J?H?|[[?xp??$??&1??8y???\W?B?H??ř`M??%D+?F:4Fu????>??$f)?]ģ*5?f?9q??6?<???":^k????????)Zݵ5???x?	??/?6?nN???r???ό??U~ier\?sq֨o?q???c??-? I?P<??0?? f???y?,U?ݺD?<q?????q???ҫ7?????T5adi?????_?@?????????՜??n}?m^]????D?????蚩??ב?{'B?????o???FC{*?A@P???nn4W
?b&??? Lfo????Y?W_>,??Y??!.9?5{??????      l      x?????? ? ?      j      x?????? ? ?     