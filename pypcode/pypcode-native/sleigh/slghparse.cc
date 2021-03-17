/* A Bison parser, made by GNU Bison 3.0.4.  */

/* Bison implementation for Yacc-like parsers in C

   Copyright (C) 1984, 1989-1990, 2000-2015 Free Software Foundation, Inc.

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */

/* As a special exception, you may create a larger work that contains
   part or all of the Bison parser skeleton and distribute that work
   under terms of your choice, so long as that work isn't itself a
   parser generator using the skeleton or a modified version thereof
   as a parser skeleton.  Alternatively, if you modify or redistribute
   the parser skeleton itself, you may (at your option) remove this
   special exception, which will cause the skeleton and the resulting
   Bison output files to be licensed under the GNU General Public
   License without this special exception.

   This special exception was added by the Free Software Foundation in
   version 2.2 of Bison.  */

/* C LALR(1) parser skeleton written by Richard Stallman, by
   simplifying the original so-called "semantic" parser.  */

/* All symbols defined below should begin with yy or YY, to avoid
   infringing on user name space.  This should be done even for local
   variables, as they might otherwise be expanded by user macros.
   There are some unavoidable exceptions within include files to
   define necessary library symbols; they are noted "INFRINGES ON
   USER NAME SPACE" below.  */

/* Identify Bison output.  */
#define YYBISON 1

/* Bison version.  */
#define YYBISON_VERSION "3.0.4"

/* Skeleton name.  */
#define YYSKELETON_NAME "yacc.c"

/* Pure parsers.  */
#define YYPURE 0

/* Push parsers.  */
#define YYPUSH 0

/* Pull parsers.  */
#define YYPULL 1




/* Copy the first part of user declarations.  */
#line 16 "slghparse.y" /* yacc.c:339  */

#include "slgh_compile.hh"

#define YYERROR_VERBOSE

  extern SleighCompile *slgh;
  extern int4 actionon;
  extern FILE *yyin;
  extern int yydebug;
  extern int yylex(void);
  extern int yyerror(const char *str );

#line 79 "slghparse.cc" /* yacc.c:339  */

# ifndef YY_NULLPTR
#  if defined __cplusplus && 201103L <= __cplusplus
#   define YY_NULLPTR nullptr
#  else
#   define YY_NULLPTR 0
#  endif
# endif

/* Enabling verbose error messages.  */
#ifdef YYERROR_VERBOSE
# undef YYERROR_VERBOSE
# define YYERROR_VERBOSE 1
#else
# define YYERROR_VERBOSE 0
#endif

/* In a future release of Bison, this section will be replaced
   by #include "slghparse.hh".  */
#ifndef YY_YY_SLGHPARSE_HH_INCLUDED
# define YY_YY_SLGHPARSE_HH_INCLUDED
/* Debug traces.  */
#ifndef YYDEBUG
# define YYDEBUG 0
#endif
#if YYDEBUG
extern int yydebug;
#endif

/* Token type.  */
#ifndef YYTOKENTYPE
# define YYTOKENTYPE
  enum yytokentype
  {
    OP_BOOL_OR = 258,
    OP_BOOL_AND = 259,
    OP_BOOL_XOR = 260,
    OP_OR = 261,
    OP_XOR = 262,
    OP_AND = 263,
    OP_EQUAL = 264,
    OP_NOTEQUAL = 265,
    OP_FEQUAL = 266,
    OP_FNOTEQUAL = 267,
    OP_GREATEQUAL = 268,
    OP_LESSEQUAL = 269,
    OP_SLESS = 270,
    OP_SGREATEQUAL = 271,
    OP_SLESSEQUAL = 272,
    OP_SGREAT = 273,
    OP_FLESS = 274,
    OP_FGREAT = 275,
    OP_FLESSEQUAL = 276,
    OP_FGREATEQUAL = 277,
    OP_LEFT = 278,
    OP_RIGHT = 279,
    OP_SRIGHT = 280,
    OP_FADD = 281,
    OP_FSUB = 282,
    OP_SDIV = 283,
    OP_SREM = 284,
    OP_FMULT = 285,
    OP_FDIV = 286,
    OP_ZEXT = 287,
    OP_CARRY = 288,
    OP_BORROW = 289,
    OP_SEXT = 290,
    OP_SCARRY = 291,
    OP_SBORROW = 292,
    OP_NAN = 293,
    OP_ABS = 294,
    OP_SQRT = 295,
    OP_CEIL = 296,
    OP_FLOOR = 297,
    OP_ROUND = 298,
    OP_INT2FLOAT = 299,
    OP_FLOAT2FLOAT = 300,
    OP_TRUNC = 301,
    OP_CPOOLREF = 302,
    OP_NEW = 303,
    OP_POPCOUNT = 304,
    BADINTEGER = 305,
    GOTO_KEY = 306,
    CALL_KEY = 307,
    RETURN_KEY = 308,
    IF_KEY = 309,
    DEFINE_KEY = 310,
    ATTACH_KEY = 311,
    MACRO_KEY = 312,
    SPACE_KEY = 313,
    TYPE_KEY = 314,
    RAM_KEY = 315,
    DEFAULT_KEY = 316,
    REGISTER_KEY = 317,
    ENDIAN_KEY = 318,
    WITH_KEY = 319,
    ALIGN_KEY = 320,
    OP_UNIMPL = 321,
    TOKEN_KEY = 322,
    SIGNED_KEY = 323,
    NOFLOW_KEY = 324,
    HEX_KEY = 325,
    DEC_KEY = 326,
    BIG_KEY = 327,
    LITTLE_KEY = 328,
    SIZE_KEY = 329,
    WORDSIZE_KEY = 330,
    OFFSET_KEY = 331,
    NAMES_KEY = 332,
    VALUES_KEY = 333,
    VARIABLES_KEY = 334,
    PCODEOP_KEY = 335,
    IS_KEY = 336,
    LOCAL_KEY = 337,
    DELAYSLOT_KEY = 338,
    CROSSBUILD_KEY = 339,
    EXPORT_KEY = 340,
    BUILD_KEY = 341,
    CONTEXT_KEY = 342,
    ELLIPSIS_KEY = 343,
    GLOBALSET_KEY = 344,
    BITRANGE_KEY = 345,
    CHAR = 346,
    INTEGER = 347,
    INTB = 348,
    STRING = 349,
    SYMBOLSTRING = 350,
    SPACESYM = 351,
    SECTIONSYM = 352,
    TOKENSYM = 353,
    USEROPSYM = 354,
    VALUESYM = 355,
    VALUEMAPSYM = 356,
    CONTEXTSYM = 357,
    NAMESYM = 358,
    VARSYM = 359,
    BITSYM = 360,
    SPECSYM = 361,
    VARLISTSYM = 362,
    OPERANDSYM = 363,
    STARTSYM = 364,
    ENDSYM = 365,
    MACROSYM = 366,
    LABELSYM = 367,
    SUBTABLESYM = 368
  };
#endif

/* Value type.  */
#if ! defined YYSTYPE && ! defined YYSTYPE_IS_DECLARED

union YYSTYPE
{
#line 29 "slghparse.y" /* yacc.c:355  */

  char ch;
  uintb *i;
  intb *big;
  string *str;
  vector<string> *strlist;
  vector<intb> *biglist;
  vector<ExprTree *> *param;
  SpaceQuality *spacequal;
  FieldQuality *fieldqual;
  StarQuality *starqual;
  VarnodeTpl *varnode;
  ExprTree *tree;
  vector<OpTpl *> *stmt;
  ConstructTpl *sem;
  SectionVector *sectionstart;
  Constructor *construct;
  PatternEquation *pateq;
  PatternExpression *patexp;

  vector<SleighSymbol *> *symlist;
  vector<ContextChange *> *contop;
  SleighSymbol *anysym;
  SpaceSymbol *spacesym;
  SectionSymbol *sectionsym;
  TokenSymbol *tokensym;
  UserOpSymbol *useropsym;
  MacroSymbol *macrosym;
  LabelSymbol *labelsym;
  SubtableSymbol *subtablesym;
  StartSymbol *startsym;
  EndSymbol *endsym;
  OperandSymbol *operandsym;
  VarnodeListSymbol *varlistsym;
  VarnodeSymbol *varsym;
  BitrangeSymbol *bitsym;
  NameSymbol *namesym;
  ValueSymbol *valuesym;
  ValueMapSymbol *valuemapsym;
  ContextSymbol *contextsym;
  FamilySymbol *famsym;
  SpecificSymbol *specsym;

#line 277 "slghparse.cc" /* yacc.c:355  */
};

typedef union YYSTYPE YYSTYPE;
# define YYSTYPE_IS_TRIVIAL 1
# define YYSTYPE_IS_DECLARED 1
#endif


extern YYSTYPE yylval;

int yyparse (void);

#endif /* !YY_YY_SLGHPARSE_HH_INCLUDED  */

/* Copy the second part of user declarations.  */

#line 294 "slghparse.cc" /* yacc.c:358  */

#ifdef short
# undef short
#endif

#ifdef YYTYPE_UINT8
typedef YYTYPE_UINT8 yytype_uint8;
#else
typedef unsigned char yytype_uint8;
#endif

#ifdef YYTYPE_INT8
typedef YYTYPE_INT8 yytype_int8;
#else
typedef signed char yytype_int8;
#endif

#ifdef YYTYPE_UINT16
typedef YYTYPE_UINT16 yytype_uint16;
#else
typedef unsigned short int yytype_uint16;
#endif

#ifdef YYTYPE_INT16
typedef YYTYPE_INT16 yytype_int16;
#else
typedef short int yytype_int16;
#endif

#ifndef YYSIZE_T
# ifdef __SIZE_TYPE__
#  define YYSIZE_T __SIZE_TYPE__
# elif defined size_t
#  define YYSIZE_T size_t
# elif ! defined YYSIZE_T
#  include <stddef.h> /* INFRINGES ON USER NAME SPACE */
#  define YYSIZE_T size_t
# else
#  define YYSIZE_T unsigned int
# endif
#endif

#define YYSIZE_MAXIMUM ((YYSIZE_T) -1)

#ifndef YY_
# if defined YYENABLE_NLS && YYENABLE_NLS
#  if ENABLE_NLS
#   include <libintl.h> /* INFRINGES ON USER NAME SPACE */
#   define YY_(Msgid) dgettext ("bison-runtime", Msgid)
#  endif
# endif
# ifndef YY_
#  define YY_(Msgid) Msgid
# endif
#endif

#ifndef YY_ATTRIBUTE
# if (defined __GNUC__                                               \
      && (2 < __GNUC__ || (__GNUC__ == 2 && 96 <= __GNUC_MINOR__)))  \
     || defined __SUNPRO_C && 0x5110 <= __SUNPRO_C
#  define YY_ATTRIBUTE(Spec) __attribute__(Spec)
# else
#  define YY_ATTRIBUTE(Spec) /* empty */
# endif
#endif

#ifndef YY_ATTRIBUTE_PURE
# define YY_ATTRIBUTE_PURE   YY_ATTRIBUTE ((__pure__))
#endif

#ifndef YY_ATTRIBUTE_UNUSED
# define YY_ATTRIBUTE_UNUSED YY_ATTRIBUTE ((__unused__))
#endif

#if !defined _Noreturn \
     && (!defined __STDC_VERSION__ || __STDC_VERSION__ < 201112)
# if defined _MSC_VER && 1200 <= _MSC_VER
#  define _Noreturn __declspec (noreturn)
# else
#  define _Noreturn YY_ATTRIBUTE ((__noreturn__))
# endif
#endif

/* Suppress unused-variable warnings by "using" E.  */
#if ! defined lint || defined __GNUC__
# define YYUSE(E) ((void) (E))
#else
# define YYUSE(E) /* empty */
#endif

#if defined __GNUC__ && 407 <= __GNUC__ * 100 + __GNUC_MINOR__
/* Suppress an incorrect diagnostic about yylval being uninitialized.  */
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN \
    _Pragma ("GCC diagnostic push") \
    _Pragma ("GCC diagnostic ignored \"-Wuninitialized\"")\
    _Pragma ("GCC diagnostic ignored \"-Wmaybe-uninitialized\"")
# define YY_IGNORE_MAYBE_UNINITIALIZED_END \
    _Pragma ("GCC diagnostic pop")
#else
# define YY_INITIAL_VALUE(Value) Value
#endif
#ifndef YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
# define YY_IGNORE_MAYBE_UNINITIALIZED_END
#endif
#ifndef YY_INITIAL_VALUE
# define YY_INITIAL_VALUE(Value) /* Nothing. */
#endif


#if ! defined yyoverflow || YYERROR_VERBOSE

/* The parser invokes alloca or malloc; define the necessary symbols.  */

# ifdef YYSTACK_USE_ALLOCA
#  if YYSTACK_USE_ALLOCA
#   ifdef __GNUC__
#    define YYSTACK_ALLOC __builtin_alloca
#   elif defined __BUILTIN_VA_ARG_INCR
#    include <alloca.h> /* INFRINGES ON USER NAME SPACE */
#   elif defined _AIX
#    define YYSTACK_ALLOC __alloca
#   elif defined _MSC_VER
#    include <malloc.h> /* INFRINGES ON USER NAME SPACE */
#    define alloca _alloca
#   else
#    define YYSTACK_ALLOC alloca
#    if ! defined _ALLOCA_H && ! defined EXIT_SUCCESS
#     include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
      /* Use EXIT_SUCCESS as a witness for stdlib.h.  */
#     ifndef EXIT_SUCCESS
#      define EXIT_SUCCESS 0
#     endif
#    endif
#   endif
#  endif
# endif

# ifdef YYSTACK_ALLOC
   /* Pacify GCC's 'empty if-body' warning.  */
#  define YYSTACK_FREE(Ptr) do { /* empty */; } while (0)
#  ifndef YYSTACK_ALLOC_MAXIMUM
    /* The OS might guarantee only one guard page at the bottom of the stack,
       and a page size can be as small as 4096 bytes.  So we cannot safely
       invoke alloca (N) if N exceeds 4096.  Use a slightly smaller number
       to allow for a few compiler-allocated temporary stack slots.  */
#   define YYSTACK_ALLOC_MAXIMUM 4032 /* reasonable circa 2006 */
#  endif
# else
#  define YYSTACK_ALLOC YYMALLOC
#  define YYSTACK_FREE YYFREE
#  ifndef YYSTACK_ALLOC_MAXIMUM
#   define YYSTACK_ALLOC_MAXIMUM YYSIZE_MAXIMUM
#  endif
#  if (defined __cplusplus && ! defined EXIT_SUCCESS \
       && ! ((defined YYMALLOC || defined malloc) \
             && (defined YYFREE || defined free)))
#   include <stdlib.h> /* INFRINGES ON USER NAME SPACE */
#   ifndef EXIT_SUCCESS
#    define EXIT_SUCCESS 0
#   endif
#  endif
#  ifndef YYMALLOC
#   define YYMALLOC malloc
#   if ! defined malloc && ! defined EXIT_SUCCESS
void *malloc (YYSIZE_T); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
#  ifndef YYFREE
#   define YYFREE free
#   if ! defined free && ! defined EXIT_SUCCESS
void free (void *); /* INFRINGES ON USER NAME SPACE */
#   endif
#  endif
# endif
#endif /* ! defined yyoverflow || YYERROR_VERBOSE */


#if (! defined yyoverflow \
     && (! defined __cplusplus \
         || (defined YYSTYPE_IS_TRIVIAL && YYSTYPE_IS_TRIVIAL)))

/* A type that is properly aligned for any stack member.  */
union yyalloc
{
  yytype_int16 yyss_alloc;
  YYSTYPE yyvs_alloc;
};

/* The size of the maximum gap between one aligned stack and the next.  */
# define YYSTACK_GAP_MAXIMUM (sizeof (union yyalloc) - 1)

/* The size of an array large to enough to hold all stacks, each with
   N elements.  */
# define YYSTACK_BYTES(N) \
     ((N) * (sizeof (yytype_int16) + sizeof (YYSTYPE)) \
      + YYSTACK_GAP_MAXIMUM)

# define YYCOPY_NEEDED 1

/* Relocate STACK from its old location to the new one.  The
   local variables YYSIZE and YYSTACKSIZE give the old and new number of
   elements in the stack, and YYPTR gives the new location of the
   stack.  Advance YYPTR to a properly aligned location for the next
   stack.  */
# define YYSTACK_RELOCATE(Stack_alloc, Stack)                           \
    do                                                                  \
      {                                                                 \
        YYSIZE_T yynewbytes;                                            \
        YYCOPY (&yyptr->Stack_alloc, Stack, yysize);                    \
        Stack = &yyptr->Stack_alloc;                                    \
        yynewbytes = yystacksize * sizeof (*Stack) + YYSTACK_GAP_MAXIMUM; \
        yyptr += yynewbytes / sizeof (*yyptr);                          \
      }                                                                 \
    while (0)

#endif

#if defined YYCOPY_NEEDED && YYCOPY_NEEDED
/* Copy COUNT objects from SRC to DST.  The source and destination do
   not overlap.  */
# ifndef YYCOPY
#  if defined __GNUC__ && 1 < __GNUC__
#   define YYCOPY(Dst, Src, Count) \
      __builtin_memcpy (Dst, Src, (Count) * sizeof (*(Src)))
#  else
#   define YYCOPY(Dst, Src, Count)              \
      do                                        \
        {                                       \
          YYSIZE_T yyi;                         \
          for (yyi = 0; yyi < (Count); yyi++)   \
            (Dst)[yyi] = (Src)[yyi];            \
        }                                       \
      while (0)
#  endif
# endif
#endif /* !YYCOPY_NEEDED */

/* YYFINAL -- State number of the termination state.  */
#define YYFINAL  5
/* YYLAST -- Last index in YYTABLE.  */
#define YYLAST   2575

/* YYNTOKENS -- Number of terminals.  */
#define YYNTOKENS  137
/* YYNNTS -- Number of nonterminals.  */
#define YYNNTS  71
/* YYNRULES -- Number of rules.  */
#define YYNRULES  336
/* YYNSTATES -- Number of states.  */
#define YYNSTATES  709

/* YYTRANSLATE[YYX] -- Symbol number corresponding to YYX as returned
   by yylex, with out-of-bounds checking.  */
#define YYUNDEFTOK  2
#define YYMAXUTOK   368

#define YYTRANSLATE(YYX)                                                \
  ((unsigned int) (YYX) <= YYMAXUTOK ? yytranslate[YYX] : YYUNDEFTOK)

/* YYTRANSLATE[TOKEN-NUM] -- Symbol number corresponding to TOKEN-NUM
   as returned by yylex, without out-of-bounds checking.  */
static const yytype_uint8 yytranslate[] =
{
       0,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,   136,    43,     2,     2,     2,    38,    11,     2,
     129,   130,    36,    32,   131,    33,     2,    37,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,   135,     8,
      17,   128,    18,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,   132,     2,   133,     9,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,   134,     6,   127,    44,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     1,     2,     3,     4,
       5,     7,    10,    12,    13,    14,    15,    16,    19,    20,
      21,    22,    23,    24,    25,    26,    27,    28,    29,    30,
      31,    34,    35,    39,    40,    41,    42,    45,    46,    47,
      48,    49,    50,    51,    52,    53,    54,    55,    56,    57,
      58,    59,    60,    61,    62,    63,    64,    65,    66,    67,
      68,    69,    70,    71,    72,    73,    74,    75,    76,    77,
      78,    79,    80,    81,    82,    83,    84,    85,    86,    87,
      88,    89,    90,    91,    92,    93,    94,    95,    96,    97,
      98,    99,   100,   101,   102,   103,   104,   105,   106,   107,
     108,   109,   110,   111,   112,   113,   114,   115,   116,   117,
     118,   119,   120,   121,   122,   123,   124,   125,   126
};

#if YYDEBUG
  /* YYRLINE[YYN] -- Source line where rule number YYN was defined.  */
static const yytype_uint16 yyrline[] =
{
       0,   156,   156,   157,   158,   159,   161,   162,   163,   164,
     165,   166,   167,   168,   169,   170,   172,   173,   174,   175,
     177,   178,   180,   182,   184,   185,   186,   188,   190,   191,
     194,   195,   196,   197,   198,   200,   201,   202,   203,   204,
     205,   207,   209,   210,   211,   212,   213,   214,   215,   217,
     219,   221,   223,   224,   226,   229,   231,   233,   235,   237,
     240,   242,   243,   244,   246,   248,   249,   250,   253,   254,
     257,   259,   260,   261,   263,   264,   266,   267,   268,   269,
     270,   271,   272,   273,   274,   276,   277,   278,   279,   281,
     283,   286,   287,   288,   289,   290,   291,   292,   293,   294,
     295,   296,   297,   298,   300,   301,   302,   303,   305,   306,
     308,   309,   311,   312,   314,   315,   316,   317,   318,   319,
     320,   323,   324,   325,   326,   328,   329,   331,   332,   333,
     334,   335,   336,   338,   339,   341,   343,   344,   346,   347,
     348,   349,   350,   352,   353,   354,   355,   357,   358,   359,
     360,   361,   362,   363,   364,   365,   366,   367,   368,   369,
     370,   371,   372,   373,   374,   375,   376,   377,   378,   379,
     380,   381,   383,   384,   385,   386,   387,   388,   389,   390,
     391,   392,   393,   394,   395,   396,   397,   398,   399,   400,
     401,   402,   403,   404,   405,   406,   407,   408,   409,   410,
     411,   412,   413,   414,   415,   416,   417,   418,   419,   420,
     421,   422,   423,   424,   425,   426,   427,   428,   429,   430,
     431,   432,   433,   434,   435,   436,   437,   438,   439,   440,
     441,   442,   443,   444,   445,   446,   447,   448,   450,   451,
     452,   453,   455,   456,   457,   458,   459,   460,   461,   462,
     464,   465,   466,   467,   469,   470,   471,   472,   473,   475,
     476,   477,   479,   480,   482,   483,   484,   485,   486,   487,
     489,   490,   491,   492,   493,   495,   496,   497,   498,   499,
     501,   502,   504,   505,   506,   508,   509,   510,   512,   513,
     514,   517,   518,   520,   521,   522,   524,   526,   527,   528,
     529,   531,   532,   533,   535,   536,   537,   538,   539,   541,
     542,   544,   545,   547,   548,   551,   552,   553,   555,   556,
     557,   559,   560,   561,   562,   563,   564,   565,   566,   567,
     568,   569,   570,   571,   572,   573,   574
};
#endif

#if YYDEBUG || YYERROR_VERBOSE || 0
/* YYTNAME[SYMBOL-NUM] -- String name of the symbol SYMBOL-NUM.
   First, the terminals, then, starting at YYNTOKENS, nonterminals.  */
static const char *const yytname[] =
{
  "$end", "error", "$undefined", "OP_BOOL_OR", "OP_BOOL_AND",
  "OP_BOOL_XOR", "'|'", "OP_OR", "';'", "'^'", "OP_XOR", "'&'", "OP_AND",
  "OP_EQUAL", "OP_NOTEQUAL", "OP_FEQUAL", "OP_FNOTEQUAL", "'<'", "'>'",
  "OP_GREATEQUAL", "OP_LESSEQUAL", "OP_SLESS", "OP_SGREATEQUAL",
  "OP_SLESSEQUAL", "OP_SGREAT", "OP_FLESS", "OP_FGREAT", "OP_FLESSEQUAL",
  "OP_FGREATEQUAL", "OP_LEFT", "OP_RIGHT", "OP_SRIGHT", "'+'", "'-'",
  "OP_FADD", "OP_FSUB", "'*'", "'/'", "'%'", "OP_SDIV", "OP_SREM",
  "OP_FMULT", "OP_FDIV", "'!'", "'~'", "OP_ZEXT", "OP_CARRY", "OP_BORROW",
  "OP_SEXT", "OP_SCARRY", "OP_SBORROW", "OP_NAN", "OP_ABS", "OP_SQRT",
  "OP_CEIL", "OP_FLOOR", "OP_ROUND", "OP_INT2FLOAT", "OP_FLOAT2FLOAT",
  "OP_TRUNC", "OP_CPOOLREF", "OP_NEW", "OP_POPCOUNT", "BADINTEGER",
  "GOTO_KEY", "CALL_KEY", "RETURN_KEY", "IF_KEY", "DEFINE_KEY",
  "ATTACH_KEY", "MACRO_KEY", "SPACE_KEY", "TYPE_KEY", "RAM_KEY",
  "DEFAULT_KEY", "REGISTER_KEY", "ENDIAN_KEY", "WITH_KEY", "ALIGN_KEY",
  "OP_UNIMPL", "TOKEN_KEY", "SIGNED_KEY", "NOFLOW_KEY", "HEX_KEY",
  "DEC_KEY", "BIG_KEY", "LITTLE_KEY", "SIZE_KEY", "WORDSIZE_KEY",
  "OFFSET_KEY", "NAMES_KEY", "VALUES_KEY", "VARIABLES_KEY", "PCODEOP_KEY",
  "IS_KEY", "LOCAL_KEY", "DELAYSLOT_KEY", "CROSSBUILD_KEY", "EXPORT_KEY",
  "BUILD_KEY", "CONTEXT_KEY", "ELLIPSIS_KEY", "GLOBALSET_KEY",
  "BITRANGE_KEY", "CHAR", "INTEGER", "INTB", "STRING", "SYMBOLSTRING",
  "SPACESYM", "SECTIONSYM", "TOKENSYM", "USEROPSYM", "VALUESYM",
  "VALUEMAPSYM", "CONTEXTSYM", "NAMESYM", "VARSYM", "BITSYM", "SPECSYM",
  "VARLISTSYM", "OPERANDSYM", "STARTSYM", "ENDSYM", "MACROSYM", "LABELSYM",
  "SUBTABLESYM", "'}'", "'='", "'('", "')'", "','", "'['", "']'", "'{'",
  "':'", "' '", "$accept", "spec", "definition", "constructorlike",
  "endiandef", "aligndef", "tokendef", "tokenprop", "contextdef",
  "contextprop", "fielddef", "contextfielddef", "spacedef", "spaceprop",
  "varnodedef", "bitrangedef", "bitrangelist", "bitrangesingle",
  "pcodeopdef", "valueattach", "nameattach", "varattach", "macrodef",
  "withblockstart", "withblockmid", "withblock", "id_or_nil",
  "bitpat_or_nil", "macrostart", "rtlbody", "constructor",
  "constructprint", "subtablestart", "pexpression", "pequation", "elleq",
  "ellrt", "atomic", "constraint", "contextblock", "contextlist",
  "section_def", "rtlfirstsection", "rtlcontinue", "rtl", "rtlmid",
  "statement", "expr", "sizedstar", "jumpdest", "varnode",
  "integervarnode", "lhsvarnode", "label", "exportvarnode", "familysymbol",
  "specificsymbol", "charstring", "intblist", "intbpart", "stringlist",
  "stringpart", "anystringlist", "anystringpart", "valuelist", "valuepart",
  "varlist", "varpart", "paramlist", "oplist", "anysymbol", YY_NULLPTR
};
#endif

# ifdef YYPRINT
/* YYTOKNUM[NUM] -- (External) token number corresponding to the
   (internal) symbol number NUM (which must be that of a token).  */
static const yytype_uint16 yytoknum[] =
{
       0,   256,   257,   258,   259,   260,   124,   261,    59,    94,
     262,    38,   263,   264,   265,   266,   267,    60,    62,   268,
     269,   270,   271,   272,   273,   274,   275,   276,   277,   278,
     279,   280,    43,    45,   281,   282,    42,    47,    37,   283,
     284,   285,   286,    33,   126,   287,   288,   289,   290,   291,
     292,   293,   294,   295,   296,   297,   298,   299,   300,   301,
     302,   303,   304,   305,   306,   307,   308,   309,   310,   311,
     312,   313,   314,   315,   316,   317,   318,   319,   320,   321,
     322,   323,   324,   325,   326,   327,   328,   329,   330,   331,
     332,   333,   334,   335,   336,   337,   338,   339,   340,   341,
     342,   343,   344,   345,   346,   347,   348,   349,   350,   351,
     352,   353,   354,   355,   356,   357,   358,   359,   360,   361,
     362,   363,   364,   365,   366,   367,   368,   125,    61,    40,
      41,    44,    91,    93,   123,    58,    32
};
# endif

#define YYPACT_NINF -306

#define yypact_value_is_default(Yystate) \
  (!!((Yystate) == (-306)))

#define YYTABLE_NINF -269

#define yytable_value_is_error(Yytable_value) \
  (!!((Yytable_value) == (-269)))

  /* YYPACT[STATE-NUM] -- Index in YYTABLE of the portion describing
     STATE-NUM.  */
static const yytype_int16 yypact[] =
{
     -15,   -35,     3,  -306,   -82,  -306,     4,   409,    95,    -8,
     -74,   -29,   -10,  -306,  -306,  -306,  -306,  -306,   420,  -306,
     449,  -306,     2,  -306,  -306,  -306,  -306,  -306,  -306,  -306,
    -306,    39,  -306,   -75,  -306,    28,    54,   -16,  -306,  -306,
    2413,    49,  2431,   -71,    26,    13,   104,    76,    76,    76,
      70,  -306,  -306,    72,  -306,  -306,  -306,   138,  -306,  -306,
    -306,  -306,  -306,  -306,  -306,  -306,  -306,  -306,  -306,  -306,
    -306,  -306,  -306,  -306,   330,   143,  -306,   156,   205,   162,
    -306,   167,  -306,   172,   176,  1475,  -306,  -306,  -306,  -306,
    -306,  2288,  -306,  -306,  -306,  -306,   216,  -306,  2288,  -306,
    -306,  -306,   216,   326,   335,  -306,  -306,   246,   272,  -306,
    -306,   298,   407,  -306,   293,    50,  -306,   305,  -306,  -306,
     -27,   294,   -13,   -39,   328,  2288,   308,  -306,  -306,  -306,
     311,   313,  -306,  -306,  -306,  -306,   316,   255,   342,   347,
     329,  1678,  1445,  -306,  -306,  -306,  -306,  -306,  -306,   351,
    -306,  2288,    15,  -306,  -306,   357,  -306,    25,  -306,    15,
    -306,  -306,   473,   377,  -306,  2309,  -306,   367,  -306,  -306,
     -28,  -306,  -306,   -51,  2449,   480,   381,  -306,    62,   485,
    -306,   -60,   486,  -306,   211,   364,   261,   393,   400,   401,
     411,  -306,  -306,  -306,  -306,  -306,   281,   -41,    91,  -306,
      -9,    74,     1,  1546,  1538,   388,   327,   301,   398,   385,
      48,   392,  -306,   394,  -306,  -306,  -306,  -306,   395,   -11,
    -306,  1546,   -48,  -306,    56,  -306,    66,  -306,  1577,    19,
    2288,  2288,  2288,  -306,   -66,  -306,  1577,  1577,  1577,  1577,
    1577,  1577,   -66,  -306,   396,  -306,  -306,  -306,   413,  -306,
     438,  -306,  -306,  -306,  -306,  -306,  2334,  -306,  -306,  -306,
     434,  -306,  -306,   -22,  -306,  -306,  -306,   190,  -306,  -306,
     440,   414,   418,   419,   421,   422,  -306,  -306,   446,  -306,
    -306,   539,   550,   465,   471,  -306,   445,  -306,  -306,  -306,
    -306,  1546,   578,  -306,  1546,   581,  -306,  1546,  1546,  1546,
    1546,  1546,   458,   462,   497,   498,   500,   502,   537,   538,
     540,   542,   573,   618,   621,   654,   655,   663,   665,   696,
    -306,  1546,  1802,  1546,  -306,    43,    24,   580,   602,   617,
     378,   575,   822,  -306,  1506,   825,  -306,   827,   765,  1546,
     768,  1546,  1546,  1546,  1503,   770,   805,  1546,   806,  1577,
    1577,  -306,  1577,  1717,  -306,  -306,  -306,   300,   904,  -306,
     310,  -306,  -306,  -306,  1717,  1717,  1717,  1717,  1717,  1717,
    -306,  -306,   845,   862,  -306,  -306,  -306,  -306,   846,  -306,
    -306,  -306,  -306,  -306,  -306,  -306,  -306,   850,   886,   890,
     925,   327,  -306,  -306,   898,  -306,   926,   343,  -306,   579,
    -306,   619,  -306,  -306,  -306,  -306,  1546,  1546,  1546,  1546,
    1546,  1546,  1546,  1546,  1546,  1546,  1546,  1546,  1546,  1546,
    1546,  1546,  1546,  1546,   823,  1546,  1546,  1546,  1546,  1546,
    1546,  1546,  1546,  1546,  1546,  1546,  1546,  1546,  1546,  1546,
    1546,  1546,  1546,  1546,  1546,  1546,  1546,  1546,  1546,  1546,
    1546,  1546,  1546,  1546,  1546,  1546,  1546,  1546,  1546,  1546,
    1546,   210,  -306,   282,   965,   966,  -306,  1546,   970,  -306,
     980,   217,  1006,  -306,  1010,  1142,  -306,  1147,  -306,  -306,
    -306,  -306,  1854,  1062,  2174,   265,  1894,   279,  1546,  1021,
    1067,  1934,  1060,  -306,  -306,   289,  1577,  1577,  1577,  1577,
    1577,  1577,  1577,  1577,  1577,  1101,  -306,  1107,  1182,  -306,
    -306,  -306,    36,  1100,  1165,  -306,  1141,  1145,  1181,  1185,
    -306,  1215,  1218,  1347,  1382,  1387,   863,   700,   903,   740,
     782,   943,   983,  1023,  1063,  1103,  1143,  1183,  1223,  1263,
     299,   659,  1303,   324,  -306,  2213,  2250,  2250,  2284,  2316,
    2346,  2451,  2451,  2451,  2451,  2477,  2477,  2477,  2477,  2477,
    2477,  2477,  2477,  2477,  2477,  2477,  2477,  1723,  1723,  1723,
     433,   433,   433,   433,  -306,  -306,  -306,  -306,  -306,  -306,
    -306,  1422,  1261,  1300,  -306,  1974,    23,  1427,  1462,  1467,
     327,  -306,  -306,  -306,  1546,  1502,  1546,  -306,  1507,  2014,
    -306,  -306,  -306,  1366,  -306,   273,   478,  2361,   303,   303,
     355,   355,  -306,  -306,  1732,  1577,  1577,  1613,   243,  -306,
    -306,  1406,   -71,  -306,  -306,  -306,  -306,  1444,  -306,  -306,
    -306,  -306,  -306,  1546,  -306,  1546,  1546,  -306,  -306,  -306,
    -306,  -306,  -306,  -306,  -306,  -306,  -306,  -306,  1546,  -306,
    -306,  -306,  -306,  1446,  -306,  -306,  1546,  -306,  -306,  -306,
    -306,  2054,  -306,  2174,  -306,  -306,  1421,  1425,  1431,  1540,
    1604,  -306,  -306,  1533,  1537,  1447,  1575,  -306,  1343,  1383,
    1423,  1463,  1452,  2094,  -306,  1458,  1472,  1473,  -306,  -306,
    -306,  -306,  -306,  -306,  -306,  -306,  -306,  -306,  -306,  -306,
    1546,  1485,  1487,  2134,  1610,  1611,  -306,  -306,  -306
};

  /* YYDEFACT[STATE-NUM] -- Default reduction number in state STATE-NUM.
     Performed when YYTABLE does not specify something else to do.  Zero
     means the default is an error.  */
static const yytype_uint16 yydefact[] =
{
       0,     0,     0,     2,     0,     1,     0,     0,     0,     0,
      65,     0,     0,    87,     4,     5,     3,     6,     0,     7,
       0,     8,     0,     9,    10,    11,    12,    13,    14,    17,
      61,     0,    18,     0,    16,     0,     0,     0,    15,    19,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,    67,    66,     0,    86,    85,    23,     0,   321,   322,
     323,   324,   327,   328,   329,   330,   331,   336,   332,   333,
     334,   335,   325,   326,    25,     0,    27,     0,    29,     0,
      41,     0,    48,     0,     0,     0,    64,    62,    63,   143,
      80,     0,   280,    81,    84,    83,    82,    79,     0,    76,
      78,    88,    77,     0,     0,    42,    43,     0,     0,    26,
     292,     0,     0,    28,     0,     0,    52,     0,   302,   303,
       0,     0,     0,     0,   318,    68,     0,    32,    33,    34,
       0,     0,    37,    38,    39,    40,     0,     0,     0,     0,
       0,   138,     0,   270,   271,   272,   273,   122,   274,   121,
     124,     0,   125,   104,   109,   111,   112,   123,   281,   125,
      20,    21,     0,     0,   293,     0,    55,     0,    51,    53,
       0,   304,   305,     0,     0,     0,     0,   283,     0,     0,
     310,     0,     0,   319,     0,   125,    69,     0,     0,     0,
       0,    44,    45,    46,    47,    59,     0,     0,   241,   255,
       0,     0,     0,     0,     0,     0,     0,     0,     0,   254,
     252,     0,   275,     0,   276,   277,   278,   279,     0,   253,
     144,     0,     0,   251,     0,   171,   250,   108,     0,     0,
       0,     0,     0,   127,     0,   110,     0,     0,     0,     0,
       0,     0,     0,    22,     0,   294,   291,   295,     0,    50,
       0,   308,   306,   307,   301,   297,     0,   298,    57,   284,
       0,   285,   287,     0,    56,   312,   311,     0,    58,    70,
       0,     0,     0,     0,     0,     0,   252,   253,     0,   257,
     250,     0,     0,     0,     0,   245,   244,   249,   246,   242,
     243,     0,     0,   248,     0,     0,   168,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     235,     0,     0,     0,   172,   250,     0,     0,     0,     0,
       0,     0,   141,   269,     0,     0,   264,     0,     0,     0,
       0,   315,     0,   315,     0,     0,     0,     0,     0,     0,
       0,    89,     0,   120,    90,    91,   113,   106,   107,   105,
       0,    73,   143,    74,   115,   116,   118,   119,   117,   114,
      75,    24,     0,     0,   299,   296,   300,   286,     0,   288,
     290,   282,   314,   313,   309,   320,    60,     0,     0,     0,
       0,     0,   263,   262,     0,   240,     0,     0,   163,     0,
     166,     0,   187,   214,   200,   188,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
     315,     0,     0,   315,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,   173,     0,     0,     0,   145,     0,     0,   152,
       0,     0,     0,   265,     0,   142,   261,     0,   259,   139,
     159,   256,     0,     0,   316,     0,     0,     0,     0,     0,
       0,     0,     0,   102,   103,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,   132,     0,     0,   126,
     136,   143,     0,     0,     0,   289,     0,     0,     0,     0,
     258,   239,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,     0,     0,     0,     0,     0,     0,
       0,     0,     0,     0,   174,   203,   202,   201,   191,   189,
     190,   177,   178,   204,   205,   179,   182,   180,   181,   183,
     184,   185,   186,   206,   207,   208,   209,   192,   193,   194,
     175,   176,   210,   211,   195,   196,   198,   197,   199,   212,
     213,     0,     0,     0,   233,     0,     0,     0,     0,     0,
       0,   267,   140,   149,     0,     0,     0,   156,     0,     0,
     158,   157,   147,     0,    92,    99,   100,    98,    96,    97,
      93,    94,    95,   101,     0,     0,     0,     0,     0,    71,
     135,     0,     0,    30,    31,    35,    36,     0,   247,   165,
     167,   169,   218,     0,   217,     0,     0,   224,   215,   216,
     226,   227,   228,   223,   222,   225,   237,   229,     0,   231,
     236,   164,   232,     0,   148,   146,     0,   162,   161,   160,
     266,     0,   154,   317,   170,   153,     0,     0,     0,     0,
       0,    72,   137,     0,     0,     0,     0,   238,     0,     0,
       0,     0,     0,     0,   151,     0,     0,     0,   128,   131,
     133,   134,    54,    49,   219,   220,   221,   230,   234,   150,
       0,     0,     0,     0,     0,     0,   155,   129,   130
};

  /* YYPGOTO[NTERM-NUM].  */
static const yytype_int16 yypgoto[] =
{
    -306,  -306,  1589,  1591,  -306,  -306,  -306,  -306,  -306,  -306,
    -306,  -306,  -306,  -306,  -306,  -306,  -306,  1511,  -306,  -306,
    -306,  -306,  -306,  -306,  -306,  -306,  -306,  -306,  -306,  1393,
    -306,  -306,  -306,  -222,   -76,  -306,  1496,  -306,  -306,  -130,
    -306,  1022,  -306,  -306,  1281,  1133,  -306,  -197,  -140,  -196,
     -62,  1184,  1312,  -139,  -306,   -91,   -36,  1612,  -306,  -306,
    1028,  -306,  -306,  -306,   443,  -306,  -306,  -306,  -305,  -306,
       8
};

  /* YYDEFGOTO[NTERM-NUM].  */
static const yytype_int16 yydefgoto[] =
{
      -1,     2,    14,    15,     3,    16,    17,    18,    19,    20,
      74,    78,    21,    22,    23,    24,   115,   116,    25,    26,
      27,    28,    29,    30,    31,    32,    53,   185,    33,   363,
      34,    35,    36,   353,   152,   153,   154,   155,   156,   234,
     360,   620,   510,   511,   140,   141,   220,   484,   323,   292,
     324,   223,   224,   293,   335,   354,   325,    96,   179,   263,
     112,   165,   175,   256,   121,   173,   182,   267,   485,   184,
      75
};

  /* YYTABLE[YYPACT[STATE-NUM]] -- What to do in state STATE-NUM.  If
     positive, shift that token.  If negative, reduce the rule whose
     number is the opposite.  If YYTABLE_NINF, syntax error.  */
static const yytype_int16 yytable[] =
{
     157,   221,   225,     5,     6,   295,   322,   157,   197,   296,
      80,   378,    38,   361,   364,   365,   366,   367,   368,   369,
     176,   230,   159,   231,   344,   230,   232,   231,    79,   242,
     232,   655,   466,    51,   157,   249,   110,    90,   487,   236,
       6,     4,   237,   238,   239,   240,    37,   265,   106,   186,
     109,   157,    52,     1,   285,   271,   251,   266,   168,    89,
     157,   111,   252,    97,   253,   618,   281,   334,   362,   103,
     104,     7,     8,     9,    81,   229,    82,   250,   180,   222,
      10,   345,   254,   379,   282,   380,   171,   346,   172,    83,
      84,   197,   177,   181,   397,   260,   286,   399,   287,    50,
     401,   402,   403,   404,   405,   226,    54,    85,     8,     9,
      11,   381,   288,   289,   290,   540,    10,  -261,   543,   178,
     114,  -261,    91,   291,   424,    55,   462,   493,   494,    12,
     495,    39,    92,   297,   279,    93,    94,   285,    13,   157,
     157,   157,   482,   113,   329,   486,    11,   233,    98,   356,
     491,   656,   467,   241,   357,   358,   359,   114,    92,   468,
     280,    99,   100,   619,    95,    12,    86,   261,   327,   262,
     280,   336,   463,   247,    13,   464,   339,   107,   465,   286,
    -260,   287,   257,   340,   347,    47,    48,    49,   348,   118,
     101,   119,   355,   117,  -259,   288,   289,   290,  -259,   124,
     355,   355,   355,   355,   355,   355,   294,   125,   120,   526,
     527,   528,   529,   530,   531,   532,   533,   534,   535,   536,
     537,   538,   539,   283,   541,   542,   284,   197,   545,   546,
     547,   548,   549,   550,   551,   552,   553,   554,   555,   556,
     557,   558,   559,   560,   561,   562,   563,   564,   565,   566,
     567,   568,   569,   570,   571,   572,   573,   574,   575,   576,
     577,   578,   579,   580,   376,   581,   126,   230,   473,   231,
     585,   130,   232,   285,   605,   606,   607,   608,   609,   610,
     611,   612,   613,   497,   131,   498,   132,   133,   134,   135,
     136,   599,   196,   196,   280,   137,   496,   382,   478,   497,
     138,   498,   499,   500,   139,   501,   502,   383,   231,   503,
     504,   232,   330,   355,   355,   286,   355,   287,   499,   500,
     158,   501,   502,   384,   588,   503,   504,   589,   191,   520,
     192,   288,   289,   290,   160,   501,   502,   198,   196,   503,
     504,   269,   270,   161,   199,   199,   425,   426,   427,   428,
     673,   162,   429,   674,   430,   280,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   209,   209,   276,   196,
     199,   503,   504,   669,   670,   595,   596,   661,   212,   663,
     214,   163,   215,   216,   217,   164,   331,   277,   332,   598,
     596,   127,   505,   128,   129,   166,   278,   506,   212,   604,
     214,   167,   215,   216,   217,   507,   174,   333,    56,   646,
     596,   508,   209,   170,   276,   183,   678,   187,   679,   680,
     188,   199,   189,   509,   212,   190,   214,   193,   215,   216,
     217,   681,   194,   277,   650,   596,   195,    76,   235,   683,
     355,   355,   355,   355,   355,   355,   355,   355,   355,   454,
     455,   456,   457,   458,   459,   460,   523,   221,   225,   228,
      40,   243,   244,   209,   248,   276,   259,    41,   258,    42,
     498,   122,   123,   264,   268,   212,   233,   214,   272,   215,
     216,   217,    43,   703,   277,   273,   274,   499,   500,    44,
     501,   502,    45,   472,   503,   504,   275,   328,    46,   337,
     338,   341,   342,   667,   343,   373,   371,    57,   660,    58,
      59,    60,    61,    62,    63,    64,    65,    66,    67,   377,
      68,    69,    70,    71,    72,   372,    73,   385,   386,   387,
     388,   391,   389,   390,   280,   222,    77,   392,    58,    59,
      60,    61,    62,    63,    64,    65,    66,    67,   393,    68,
      69,    70,    71,    72,   394,    73,   395,   396,   668,   355,
     355,   226,   425,   426,   427,   428,   398,   406,   429,   400,
     430,   407,   431,   432,   433,   434,   435,   436,   437,   438,
     439,   440,   441,   442,   443,   444,   445,   446,   447,   448,
     449,   450,   451,   452,   453,   454,   455,   456,   457,   458,
     459,   460,   425,   426,   427,   428,   408,   409,   429,   410,
     430,   411,   431,   432,   433,   434,   435,   436,   437,   438,
     439,   440,   441,   442,   443,   444,   445,   446,   447,   448,
     449,   450,   451,   452,   453,   454,   455,   456,   457,   458,
     459,   460,   425,   426,   427,   428,   412,   413,   429,   414,
     430,   415,   431,   432,   433,   434,   435,   436,   437,   438,
     439,   440,   441,   442,   443,   444,   445,   446,   447,   448,
     449,   450,   451,   452,   453,   454,   455,   456,   457,   458,
     459,   460,   416,   425,   426,   427,   428,   470,   469,   429,
     474,   430,   524,   431,   432,   433,   434,   435,   436,   437,
     438,   439,   440,   441,   442,   443,   444,   445,   446,   447,
     448,   449,   450,   451,   452,   453,   454,   455,   456,   457,
     458,   459,   460,   425,   426,   427,   428,   417,   471,   429,
     418,   430,   525,   431,   432,   433,   434,   435,   436,   437,
     438,   439,   440,   441,   442,   443,   444,   445,   446,   447,
     448,   449,   450,   451,   452,   453,   454,   455,   456,   457,
     458,   459,   460,   419,   420,   425,   426,   427,   428,   647,
     648,   429,   421,   430,   422,   431,   432,   433,   434,   435,
     436,   437,   438,   439,   440,   441,   442,   443,   444,   445,
     446,   447,   448,   449,   450,   451,   452,   453,   454,   455,
     456,   457,   458,   459,   460,   423,   425,   426,   427,   428,
    -268,   633,   429,   479,   430,   480,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
     481,   635,   429,   483,   430,   489,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
     490,   492,   429,   636,   430,   232,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
     513,   515,   429,   544,   430,   516,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
     514,   517,   429,   632,   430,   518,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
     519,   521,   429,   634,   430,   522,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
     583,   584,   429,   637,   430,   586,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
     587,   590,   429,   638,   430,   591,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
    -260,   600,   429,   639,   430,   592,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
     594,   603,   429,   640,   430,   601,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
     614,   621,   429,   641,   430,   615,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
     622,   623,   429,   642,   430,   624,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
     616,   625,   429,   643,   430,   626,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
     627,   628,   429,   644,   430,   629,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
     630,   652,   429,   645,   430,   631,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
     651,   653,   429,   649,   430,   657,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
     658,   666,   429,   694,   430,   659,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   425,   426,   427,   428,
     662,   675,   429,   695,   430,   664,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,    40,   496,   688,   677,
     497,   682,   498,   696,   685,    42,   686,   196,   143,   144,
     145,   146,   687,   690,   147,   148,   149,   691,    43,   499,
     500,   150,   501,   502,   151,    44,   503,   504,    45,   298,
     692,   299,   198,   693,    46,   698,   700,   701,   702,   300,
     301,   302,   303,   697,   304,   305,   306,   307,   308,   309,
     310,   311,   312,   313,   314,   315,   316,   317,   318,   199,
     349,   496,   689,   475,   497,   704,   498,   705,   707,   708,
      87,   350,    88,   212,   196,   214,   169,   215,   216,   217,
     197,   488,   476,   499,   500,   370,   501,   502,   227,   672,
     503,   504,   618,   512,   617,   326,   477,   582,   102,   198,
     676,   209,     0,   276,     0,   212,     0,   214,   319,   215,
     216,   217,     0,   212,   320,   214,     0,   215,   216,   217,
       0,     0,   277,     0,     0,   321,   199,   200,   201,   202,
     203,     0,     0,   351,     0,     0,     0,     0,     0,   196,
     143,   144,   145,   146,   212,   197,   214,   148,   215,   216,
     217,     0,     0,     0,     0,     0,   352,     0,   204,   205,
     206,     0,   208,     0,   198,     0,     0,     0,   209,     0,
     210,     0,     0,     0,   496,   211,     0,   497,     0,   498,
     212,   213,   214,     0,   215,   216,   217,   218,     0,   219,
     671,   199,   200,   201,   202,   203,   499,   500,     0,   501,
     502,     0,     0,   503,   504,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,     0,     0,     0,     0,
       0,     0,     0,   204,   205,   206,   207,   208,     0,     0,
       0,     0,     0,   209,     0,   210,     0,     0,     0,     0,
     211,     0,     0,     0,     0,   212,   213,   214,     0,   215,
     216,   217,   218,     0,   219,   425,   426,   427,   428,     0,
       0,   429,     0,   430,     0,   431,   432,   433,   434,   435,
     436,   437,   438,   439,   440,   441,   442,   443,   444,   445,
     446,   447,   448,   449,   450,   451,   452,   453,   454,   455,
     456,   457,   458,   459,   460,   143,   144,   145,   146,   212,
       0,   214,   148,   215,   216,   217,     0,   425,   426,   427,
     428,     0,   593,   429,     0,   430,   461,   431,   432,   433,
     434,   435,   436,   437,   438,   439,   440,   441,   442,   443,
     444,   445,   446,   447,   448,   449,   450,   451,   452,   453,
     454,   455,   456,   457,   458,   459,   460,   425,   426,   427,
     428,     0,   597,   429,     0,   430,     0,   431,   432,   433,
     434,   435,   436,   437,   438,   439,   440,   441,   442,   443,
     444,   445,   446,   447,   448,   449,   450,   451,   452,   453,
     454,   455,   456,   457,   458,   459,   460,   425,   426,   427,
     428,     0,   602,   429,     0,   430,     0,   431,   432,   433,
     434,   435,   436,   437,   438,   439,   440,   441,   442,   443,
     444,   445,   446,   447,   448,   449,   450,   451,   452,   453,
     454,   455,   456,   457,   458,   459,   460,   425,   426,   427,
     428,     0,   654,   429,     0,   430,     0,   431,   432,   433,
     434,   435,   436,   437,   438,   439,   440,   441,   442,   443,
     444,   445,   446,   447,   448,   449,   450,   451,   452,   453,
     454,   455,   456,   457,   458,   459,   460,   425,   426,   427,
     428,     0,   665,   429,     0,   430,     0,   431,   432,   433,
     434,   435,   436,   437,   438,   439,   440,   441,   442,   443,
     444,   445,   446,   447,   448,   449,   450,   451,   452,   453,
     454,   455,   456,   457,   458,   459,   460,   425,   426,   427,
     428,     0,   684,   429,     0,   430,     0,   431,   432,   433,
     434,   435,   436,   437,   438,   439,   440,   441,   442,   443,
     444,   445,   446,   447,   448,   449,   450,   451,   452,   453,
     454,   455,   456,   457,   458,   459,   460,   425,   426,   427,
     428,     0,   699,   429,     0,   430,     0,   431,   432,   433,
     434,   435,   436,   437,   438,   439,   440,   441,   442,   443,
     444,   445,   446,   447,   448,   449,   450,   451,   452,   453,
     454,   455,   456,   457,   458,   459,   460,   425,   426,   427,
     428,     0,   706,   429,     0,   430,     0,   431,   432,   433,
     434,   435,   436,   437,   438,   439,   440,   441,   442,   443,
     444,   445,   446,   447,   448,   449,   450,   451,   452,   453,
     454,   455,   456,   457,   458,   459,   460,   425,   426,   427,
     428,     0,     0,   429,     0,   430,     0,   431,   432,   433,
     434,   435,   436,   437,   438,   439,   440,   441,   442,   443,
     444,   445,   446,   447,   448,   449,   450,   451,   452,   453,
     454,   455,   456,   457,   458,   459,   460,   426,   427,   428,
       0,     0,   429,     0,   430,     0,   431,   432,   433,   434,
     435,   436,   437,   438,   439,   440,   441,   442,   443,   444,
     445,   446,   447,   448,   449,   450,   451,   452,   453,   454,
     455,   456,   457,   458,   459,   460,   428,     0,     0,   429,
       0,   430,     0,   431,   432,   433,   434,   435,   436,   437,
     438,   439,   440,   441,   442,   443,   444,   445,   446,   447,
     448,   449,   450,   451,   452,   453,   454,   455,   456,   457,
     458,   459,   460,   429,     0,   430,     0,   431,   432,   433,
     434,   435,   436,   437,   438,   439,   440,   441,   442,   443,
     444,   445,   446,   447,   448,   449,   450,   451,   452,   453,
     454,   455,   456,   457,   458,   459,   460,   430,     0,   431,
     432,   433,   434,   435,   436,   437,   438,   439,   440,   441,
     442,   443,   444,   445,   446,   447,   448,   449,   450,   451,
     452,   453,   454,   455,   456,   457,   458,   459,   460,   431,
     432,   433,   434,   435,   436,   437,   438,   439,   440,   441,
     442,   443,   444,   445,   446,   447,   448,   449,   450,   451,
     452,   453,   454,   455,   456,   457,   458,   459,   460,   142,
     499,   500,     0,   501,   502,     0,     0,   503,   504,     0,
       0,   143,   144,   145,   146,     0,     0,   147,   148,   149,
       0,     0,     0,     0,   150,     0,   245,   151,    58,    59,
      60,    61,    62,    63,    64,    65,    66,    67,     0,    68,
      69,    70,    71,    72,     0,    73,     0,     0,     0,     0,
       0,   374,   246,    58,    59,    60,    61,    62,    63,    64,
      65,    66,    67,     0,    68,    69,    70,    71,    72,     0,
      73,     0,     0,     0,     0,     0,     0,   375,   435,   436,
     437,   438,   439,   440,   441,   442,   443,   444,   445,   446,
     447,   448,   449,   450,   451,   452,   453,   454,   455,   456,
     457,   458,   459,   460,  -269,  -269,  -269,  -269,  -269,  -269,
    -269,  -269,  -269,  -269,  -269,  -269,   447,   448,   449,   450,
     451,   452,   453,   454,   455,   456,   457,   458,   459,   460,
     105,     0,    58,    59,    60,    61,    62,    63,    64,    65,
      66,    67,     0,    68,    69,    70,    71,    72,   108,    73,
      58,    59,    60,    61,    62,    63,    64,    65,    66,    67,
       0,    68,    69,    70,    71,    72,   255,    73,    58,    59,
      60,    61,    62,    63,    64,    65,    66,    67,     0,    68,
      69,    70,    71,    72,     0,    73
};

static const yytype_int16 yycheck[] =
{
      91,   141,   141,     0,     1,   201,   203,    98,    17,     8,
       8,    33,     8,    79,   236,   237,   238,   239,   240,   241,
      33,     6,    98,     8,   221,     6,    11,     8,    20,   159,
      11,     8,     8,   107,   125,    63,   107,     9,   343,    14,
       1,    76,    17,    18,    19,    20,   128,   107,    40,   125,
      42,   142,   126,    68,    63,   185,   107,   117,     8,   134,
     151,   132,   113,     9,   115,    29,   107,   207,   134,    85,
      86,    68,    69,    70,    72,   151,    74,   105,   117,   141,
      77,   129,   133,   105,   125,   107,   113,   135,   115,    87,
      88,    17,   105,   132,   291,    33,   105,   294,   107,   107,
     297,   298,   299,   300,   301,   141,   135,    68,    69,    70,
     107,   133,   121,   122,   123,   420,    77,   128,   423,   132,
     107,   132,    94,   132,   321,   135,   323,   349,   350,   126,
     352,   127,   104,   132,   196,   107,   108,    63,   135,   230,
     231,   232,   339,   117,   206,   342,   107,   132,    94,   130,
     347,   128,   128,   128,   230,   231,   232,   107,   104,   135,
     196,   107,   108,   127,   136,   126,   127,   105,   204,   107,
     206,   207,   129,   165,   135,   132,   128,   128,   135,   105,
     132,   107,   174,   135,   128,    90,    91,    92,   132,   113,
     136,   115,   228,    89,   128,   121,   122,   123,   132,   129,
     236,   237,   238,   239,   240,   241,   132,   135,   132,   406,
     407,   408,   409,   410,   411,   412,   413,   414,   415,   416,
     417,   418,   419,   132,   421,   422,   135,    17,   425,   426,
     427,   428,   429,   430,   431,   432,   433,   434,   435,   436,
     437,   438,   439,   440,   441,   442,   443,   444,   445,   446,
     447,   448,   449,   450,   451,   452,   453,   454,   455,   456,
     457,   458,   459,   460,   256,   461,   128,     6,   330,     8,
     467,   128,    11,    63,   496,   497,   498,   499,   500,   501,
     502,   503,   504,    10,   128,    12,    81,    82,    83,    84,
     128,   488,    11,    11,   330,   128,     7,   107,   334,    10,
     128,    12,    29,    30,   128,    32,    33,   117,     8,    36,
      37,    11,    11,   349,   350,   105,   352,   107,    29,    30,
     104,    32,    33,   133,   107,    36,    37,   110,    73,   391,
      75,   121,   122,   123,     8,    32,    33,    36,    11,    36,
      37,   130,   131,     8,    63,    63,     3,     4,     5,     6,
     107,   105,     9,   110,    11,   391,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,   105,   105,   107,    11,
      63,    36,    37,   615,   616,   130,   131,   594,   117,   596,
     119,   129,   121,   122,   123,   107,   105,   126,   107,   130,
     131,    81,   102,    83,    84,     8,   135,   107,   117,   130,
     119,   128,   121,   122,   123,   115,   132,   126,     8,   130,
     131,   121,   105,   128,   107,   107,   633,   129,   635,   636,
     129,    63,   129,   133,   117,   129,   119,   105,   121,   122,
     123,   648,   105,   126,   130,   131,   127,     8,   101,   656,
     496,   497,   498,   499,   500,   501,   502,   503,   504,    36,
      37,    38,    39,    40,    41,    42,   133,   617,   617,   128,
      71,     8,   105,   105,   117,   107,   105,    78,     8,    80,
      12,    48,    49,     8,     8,   117,   132,   119,   105,   121,
     122,   123,    93,   700,   126,   105,   105,    29,    30,   100,
      32,    33,   103,   135,    36,    37,   105,   129,   109,   121,
     135,   129,   128,   614,   129,    87,   130,   107,   590,   109,
     110,   111,   112,   113,   114,   115,   116,   117,   118,   105,
     120,   121,   122,   123,   124,   132,   126,   107,   134,   131,
     131,   105,   131,   131,   590,   617,   107,    18,   109,   110,
     111,   112,   113,   114,   115,   116,   117,   118,    18,   120,
     121,   122,   123,   124,   109,   126,   105,   132,   614,   615,
     616,   617,     3,     4,     5,     6,     8,   129,     9,     8,
      11,   129,    13,    14,    15,    16,    17,    18,    19,    20,
      21,    22,    23,    24,    25,    26,    27,    28,    29,    30,
      31,    32,    33,    34,    35,    36,    37,    38,    39,    40,
      41,    42,     3,     4,     5,     6,   129,   129,     9,   129,
      11,   129,    13,    14,    15,    16,    17,    18,    19,    20,
      21,    22,    23,    24,    25,    26,    27,    28,    29,    30,
      31,    32,    33,    34,    35,    36,    37,    38,    39,    40,
      41,    42,     3,     4,     5,     6,   129,   129,     9,   129,
      11,   129,    13,    14,    15,    16,    17,    18,    19,    20,
      21,    22,    23,    24,    25,    26,    27,    28,    29,    30,
      31,    32,    33,    34,    35,    36,    37,    38,    39,    40,
      41,    42,   129,     3,     4,     5,     6,   105,   128,     9,
     135,    11,   133,    13,    14,    15,    16,    17,    18,    19,
      20,    21,    22,    23,    24,    25,    26,    27,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,    41,    42,     3,     4,     5,     6,   129,   131,     9,
     129,    11,   133,    13,    14,    15,    16,    17,    18,    19,
      20,    21,    22,    23,    24,    25,    26,    27,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,    41,    42,   129,   129,     3,     4,     5,     6,   130,
     131,     9,   129,    11,   129,    13,    14,    15,    16,    17,
      18,    19,    20,    21,    22,    23,    24,    25,    26,    27,
      28,    29,    30,    31,    32,    33,    34,    35,    36,    37,
      38,    39,    40,    41,    42,   129,     3,     4,     5,     6,
       8,   131,     9,     8,    11,     8,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
     105,   131,     9,   105,    11,   105,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
     105,   105,     9,   131,    11,    11,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
     105,   105,     9,   130,    11,   105,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
     128,   105,     9,   130,    11,   105,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
     105,   133,     9,   130,    11,   109,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
     105,   105,     9,   130,    11,   105,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
     130,   105,     9,   130,    11,   105,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
       8,   130,     9,   130,    11,     8,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
     128,   131,     9,   130,    11,   128,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
     129,   131,     9,   130,    11,   128,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
     105,   130,     9,   130,    11,   130,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
     128,   130,     9,   130,    11,   130,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
     135,   133,     9,   130,    11,     8,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
       8,   130,     9,   130,    11,     8,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
       8,   131,     9,   130,    11,     8,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
       8,   105,     9,   130,    11,     8,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     3,     4,     5,     6,
       8,   105,     9,   130,    11,     8,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,    71,     7,     8,   105,
      10,   105,    12,   130,   133,    80,   131,    11,   113,   114,
     115,   116,   131,    30,   119,   120,   121,    30,    93,    29,
      30,   126,    32,    33,   129,   100,    36,    37,   103,    33,
     133,    35,    36,     8,   109,   133,   128,   115,   115,    43,
      44,    45,    46,   130,    48,    49,    50,    51,    52,    53,
      54,    55,    56,    57,    58,    59,    60,    61,    62,    63,
      33,     7,     8,   107,    10,   130,    12,   130,     8,     8,
      31,    44,    31,   117,    11,   119,   115,   121,   122,   123,
      17,   128,   126,    29,    30,   242,    32,    33,   142,   617,
      36,    37,    29,   362,   511,   107,   334,   463,    36,    36,
     622,   105,    -1,   107,    -1,   117,    -1,   119,   112,   121,
     122,   123,    -1,   117,   118,   119,    -1,   121,   122,   123,
      -1,    -1,   126,    -1,    -1,   129,    63,    64,    65,    66,
      67,    -1,    -1,   106,    -1,    -1,    -1,    -1,    -1,    11,
     113,   114,   115,   116,   117,    17,   119,   120,   121,   122,
     123,    -1,    -1,    -1,    -1,    -1,   129,    -1,    95,    96,
      97,    -1,    99,    -1,    36,    -1,    -1,    -1,   105,    -1,
     107,    -1,    -1,    -1,     7,   112,    -1,    10,    -1,    12,
     117,   118,   119,    -1,   121,   122,   123,   124,    -1,   126,
     127,    63,    64,    65,    66,    67,    29,    30,    -1,    32,
      33,    -1,    -1,    36,    37,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,    -1,    -1,    -1,    -1,
      -1,    -1,    -1,    95,    96,    97,    98,    99,    -1,    -1,
      -1,    -1,    -1,   105,    -1,   107,    -1,    -1,    -1,    -1,
     112,    -1,    -1,    -1,    -1,   117,   118,   119,    -1,   121,
     122,   123,   124,    -1,   126,     3,     4,     5,     6,    -1,
      -1,     9,    -1,    11,    -1,    13,    14,    15,    16,    17,
      18,    19,    20,    21,    22,    23,    24,    25,    26,    27,
      28,    29,    30,    31,    32,    33,    34,    35,    36,    37,
      38,    39,    40,    41,    42,   113,   114,   115,   116,   117,
      -1,   119,   120,   121,   122,   123,    -1,     3,     4,     5,
       6,    -1,     8,     9,    -1,    11,    64,    13,    14,    15,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      26,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,     3,     4,     5,
       6,    -1,     8,     9,    -1,    11,    -1,    13,    14,    15,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      26,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,     3,     4,     5,
       6,    -1,     8,     9,    -1,    11,    -1,    13,    14,    15,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      26,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,     3,     4,     5,
       6,    -1,     8,     9,    -1,    11,    -1,    13,    14,    15,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      26,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,     3,     4,     5,
       6,    -1,     8,     9,    -1,    11,    -1,    13,    14,    15,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      26,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,     3,     4,     5,
       6,    -1,     8,     9,    -1,    11,    -1,    13,    14,    15,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      26,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,     3,     4,     5,
       6,    -1,     8,     9,    -1,    11,    -1,    13,    14,    15,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      26,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,     3,     4,     5,
       6,    -1,     8,     9,    -1,    11,    -1,    13,    14,    15,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      26,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,     3,     4,     5,
       6,    -1,    -1,     9,    -1,    11,    -1,    13,    14,    15,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      26,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,     4,     5,     6,
      -1,    -1,     9,    -1,    11,    -1,    13,    14,    15,    16,
      17,    18,    19,    20,    21,    22,    23,    24,    25,    26,
      27,    28,    29,    30,    31,    32,    33,    34,    35,    36,
      37,    38,    39,    40,    41,    42,     6,    -1,    -1,     9,
      -1,    11,    -1,    13,    14,    15,    16,    17,    18,    19,
      20,    21,    22,    23,    24,    25,    26,    27,    28,    29,
      30,    31,    32,    33,    34,    35,    36,    37,    38,    39,
      40,    41,    42,     9,    -1,    11,    -1,    13,    14,    15,
      16,    17,    18,    19,    20,    21,    22,    23,    24,    25,
      26,    27,    28,    29,    30,    31,    32,    33,    34,    35,
      36,    37,    38,    39,    40,    41,    42,    11,    -1,    13,
      14,    15,    16,    17,    18,    19,    20,    21,    22,    23,
      24,    25,    26,    27,    28,    29,    30,    31,    32,    33,
      34,    35,    36,    37,    38,    39,    40,    41,    42,    13,
      14,    15,    16,    17,    18,    19,    20,    21,    22,    23,
      24,    25,    26,    27,    28,    29,    30,    31,    32,    33,
      34,    35,    36,    37,    38,    39,    40,    41,    42,   101,
      29,    30,    -1,    32,    33,    -1,    -1,    36,    37,    -1,
      -1,   113,   114,   115,   116,    -1,    -1,   119,   120,   121,
      -1,    -1,    -1,    -1,   126,    -1,   107,   129,   109,   110,
     111,   112,   113,   114,   115,   116,   117,   118,    -1,   120,
     121,   122,   123,   124,    -1,   126,    -1,    -1,    -1,    -1,
      -1,   107,   133,   109,   110,   111,   112,   113,   114,   115,
     116,   117,   118,    -1,   120,   121,   122,   123,   124,    -1,
     126,    -1,    -1,    -1,    -1,    -1,    -1,   133,    17,    18,
      19,    20,    21,    22,    23,    24,    25,    26,    27,    28,
      29,    30,    31,    32,    33,    34,    35,    36,    37,    38,
      39,    40,    41,    42,    17,    18,    19,    20,    21,    22,
      23,    24,    25,    26,    27,    28,    29,    30,    31,    32,
      33,    34,    35,    36,    37,    38,    39,    40,    41,    42,
     107,    -1,   109,   110,   111,   112,   113,   114,   115,   116,
     117,   118,    -1,   120,   121,   122,   123,   124,   107,   126,
     109,   110,   111,   112,   113,   114,   115,   116,   117,   118,
      -1,   120,   121,   122,   123,   124,   107,   126,   109,   110,
     111,   112,   113,   114,   115,   116,   117,   118,    -1,   120,
     121,   122,   123,   124,    -1,   126
};

  /* YYSTOS[STATE-NUM] -- The (internal number of the) accessing
     symbol of state STATE-NUM.  */
static const yytype_uint8 yystos[] =
{
       0,    68,   138,   141,    76,     0,     1,    68,    69,    70,
      77,   107,   126,   135,   139,   140,   142,   143,   144,   145,
     146,   149,   150,   151,   152,   155,   156,   157,   158,   159,
     160,   161,   162,   165,   167,   168,   169,   128,     8,   127,
      71,    78,    80,    93,   100,   103,   109,    90,    91,    92,
     107,   107,   126,   163,   135,   135,     8,   107,   109,   110,
     111,   112,   113,   114,   115,   116,   117,   118,   120,   121,
     122,   123,   124,   126,   147,   207,     8,   107,   148,   207,
       8,    72,    74,    87,    88,    68,   127,   139,   140,   134,
       9,    94,   104,   107,   108,   136,   194,     9,    94,   107,
     108,   136,   194,    85,    86,   107,   207,   128,   107,   207,
     107,   132,   197,   117,   107,   153,   154,    89,   113,   115,
     132,   201,   201,   201,   129,   135,   128,    81,    83,    84,
     128,   128,    81,    82,    83,    84,   128,   128,   128,   128,
     181,   182,   101,   113,   114,   115,   116,   119,   120,   121,
     126,   129,   171,   172,   173,   174,   175,   192,   104,   171,
       8,     8,   105,   129,   107,   198,     8,   128,     8,   154,
     128,   113,   115,   202,   132,   199,    33,   105,   132,   195,
     117,   132,   203,   107,   206,   164,   171,   129,   129,   129,
     129,    73,    75,   105,   105,   127,    11,    17,    36,    63,
      64,    65,    66,    67,    95,    96,    97,    98,    99,   105,
     107,   112,   117,   118,   119,   121,   122,   123,   124,   126,
     183,   185,   187,   188,   189,   190,   193,   173,   128,   171,
       6,     8,    11,   132,   176,   101,    14,    17,    18,    19,
      20,   128,   176,     8,   105,   107,   133,   207,   117,    63,
     105,   107,   113,   115,   133,   107,   200,   207,     8,   105,
      33,   105,   107,   196,     8,   107,   117,   204,     8,   130,
     131,   176,   105,   105,   105,   105,   107,   126,   135,   187,
     193,   107,   125,   132,   135,    63,   105,   107,   121,   122,
     123,   132,   186,   190,   132,   186,     8,   132,    33,    35,
      43,    44,    45,    46,    48,    49,    50,    51,    52,    53,
      54,    55,    56,    57,    58,    59,    60,    61,    62,   112,
     118,   129,   184,   185,   187,   193,   107,   193,   129,   187,
      11,   105,   107,   126,   185,   191,   193,   121,   135,   128,
     135,   129,   128,   129,   184,   129,   135,   128,   132,    33,
      44,   106,   129,   170,   192,   193,   130,   171,   171,   171,
     177,    79,   134,   166,   170,   170,   170,   170,   170,   170,
     166,   130,   132,    87,   107,   133,   207,   105,    33,   105,
     107,   133,   107,   117,   133,   107,   134,   131,   131,   131,
     131,   105,    18,    18,   109,   105,   132,   184,     8,   184,
       8,   184,   184,   184,   184,   184,   129,   129,   129,   129,
     129,   129,   129,   129,   129,   129,   129,   129,   129,   129,
     129,   129,   129,   129,   184,     3,     4,     5,     6,     9,
      11,    13,    14,    15,    16,    17,    18,    19,    20,    21,
      22,    23,    24,    25,    26,    27,    28,    29,    30,    31,
      32,    33,    34,    35,    36,    37,    38,    39,    40,    41,
      42,    64,   184,   129,   132,   135,     8,   128,   135,   128,
     105,   131,   135,   187,   135,   107,   126,   189,   193,     8,
       8,   105,   184,   105,   184,   205,   184,   205,   128,   105,
     105,   184,   105,   170,   170,   170,     7,    10,    12,    29,
      30,    32,    33,    36,    37,   102,   107,   115,   121,   133,
     179,   180,   181,   105,   128,   105,   105,   105,   105,   105,
     187,   133,   109,   133,   133,   133,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     205,   184,   184,   205,   130,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   186,   188,   105,   105,   184,   105,   130,   107,   110,
     105,   105,     8,     8,   128,   130,   131,     8,   130,   184,
     130,   128,     8,   131,   130,   170,   170,   170,   170,   170,
     170,   170,   170,   170,   129,   128,   128,   182,    29,   127,
     178,   131,   105,   130,   130,   130,   130,   135,   133,     8,
       8,     8,   130,   131,   130,   131,   131,   130,   130,   130,
     130,   130,   130,   130,   130,   130,   130,   130,   131,   130,
     130,     8,   130,   131,     8,     8,   128,     8,     8,     8,
     187,   184,     8,   184,     8,     8,   105,   192,   193,   170,
     170,   127,   178,   107,   110,   105,   197,   105,   184,   184,
     184,   184,   105,   184,     8,   133,   131,   131,     8,     8,
      30,    30,   133,     8,   130,   130,   130,   130,   133,     8,
     128,   115,   115,   184,   130,   130,     8,     8,     8
};

  /* YYR1[YYN] -- Symbol number of symbol that rule YYN derives.  */
static const yytype_uint8 yyr1[] =
{
       0,   137,   138,   138,   138,   138,   139,   139,   139,   139,
     139,   139,   139,   139,   139,   139,   140,   140,   140,   140,
     141,   141,   142,   143,   144,   144,   144,   145,   146,   146,
     147,   147,   147,   147,   147,   148,   148,   148,   148,   148,
     148,   149,   150,   150,   150,   150,   150,   150,   150,   151,
     151,   152,   153,   153,   154,   155,   156,   157,   158,   159,
     160,   161,   161,   161,   162,   163,   163,   163,   164,   164,
     165,   166,   166,   166,   167,   167,   168,   168,   168,   168,
     168,   168,   168,   168,   168,   169,   169,   169,   169,   170,
     170,   170,   170,   170,   170,   170,   170,   170,   170,   170,
     170,   170,   170,   170,   171,   171,   171,   171,   172,   172,
     173,   173,   174,   174,   175,   175,   175,   175,   175,   175,
     175,   175,   175,   175,   175,   176,   176,   177,   177,   177,
     177,   177,   177,   178,   178,   179,   180,   180,   181,   181,
     181,   181,   181,   182,   182,   182,   182,   183,   183,   183,
     183,   183,   183,   183,   183,   183,   183,   183,   183,   183,
     183,   183,   183,   183,   183,   183,   183,   183,   183,   183,
     183,   183,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   184,   184,
     184,   184,   184,   184,   184,   184,   184,   184,   185,   185,
     185,   185,   186,   186,   186,   186,   186,   186,   186,   186,
     187,   187,   187,   187,   188,   188,   188,   188,   188,   189,
     189,   189,   190,   190,   191,   191,   191,   191,   191,   191,
     192,   192,   192,   192,   192,   193,   193,   193,   193,   193,
     194,   194,   195,   195,   195,   196,   196,   196,   196,   196,
     196,   197,   197,   198,   198,   198,   199,   200,   200,   200,
     200,   201,   201,   201,   202,   202,   202,   202,   202,   203,
     203,   204,   204,   204,   204,   205,   205,   205,   206,   206,
     206,   207,   207,   207,   207,   207,   207,   207,   207,   207,
     207,   207,   207,   207,   207,   207,   207
};

  /* YYR2[YYN] -- Number of symbols on the right hand side of rule YYN.  */
static const yytype_uint8 yyr2[] =
{
       0,     2,     1,     2,     2,     2,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     2,     1,     1,     1,     2,
       5,     5,     5,     2,     6,     2,     3,     2,     3,     2,
       7,     7,     2,     2,     2,     7,     7,     2,     2,     2,
       2,     2,     3,     3,     4,     4,     4,     4,     2,    10,
       5,     4,     1,     2,     8,     4,     5,     5,     5,     4,
       6,     1,     2,     2,     2,     0,     1,     1,     0,     1,
       5,     3,     4,     1,     5,     5,     2,     2,     2,     2,
       2,     2,     2,     2,     2,     2,     2,     1,     2,     1,
       1,     1,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     2,     2,     1,     3,     3,     3,     2,     1,
       2,     1,     1,     3,     3,     3,     3,     3,     3,     3,
       3,     1,     1,     1,     1,     0,     3,     0,     5,     8,
       8,     5,     2,     3,     3,     2,     1,     3,     1,     4,
       5,     3,     4,     0,     2,     4,     6,     4,     5,     4,
       7,     6,     3,     5,     5,     9,     4,     4,     4,     3,
       5,     5,     5,     3,     5,     5,     3,     5,     2,     5,
       5,     1,     1,     2,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     3,     3,     3,     2,     2,     3,
       3,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       2,     3,     3,     3,     3,     3,     3,     3,     3,     3,
       3,     3,     3,     3,     2,     4,     4,     4,     4,     6,
       6,     6,     4,     4,     4,     4,     4,     4,     4,     4,
       6,     4,     4,     3,     6,     1,     4,     4,     6,     4,
       3,     1,     1,     1,     1,     1,     1,     4,     1,     1,
       1,     1,     1,     1,     1,     1,     3,     2,     4,     1,
       1,     1,     3,     3,     1,     2,     4,     3,     1,     1,
       1,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     2,     3,     1,     2,     1,     2,     1,     2,     3,
       2,     3,     1,     1,     2,     2,     3,     1,     1,     2,
       2,     3,     1,     1,     1,     1,     2,     2,     2,     3,
       1,     1,     1,     2,     2,     0,     1,     3,     0,     1,
       3,     1,     1,     1,     1,     1,     1,     1,     1,     1,
       1,     1,     1,     1,     1,     1,     1
};


#define yyerrok         (yyerrstatus = 0)
#define yyclearin       (yychar = YYEMPTY)
#define YYEMPTY         (-2)
#define YYEOF           0

#define YYACCEPT        goto yyacceptlab
#define YYABORT         goto yyabortlab
#define YYERROR         goto yyerrorlab


#define YYRECOVERING()  (!!yyerrstatus)

#define YYBACKUP(Token, Value)                                  \
do                                                              \
  if (yychar == YYEMPTY)                                        \
    {                                                           \
      yychar = (Token);                                         \
      yylval = (Value);                                         \
      YYPOPSTACK (yylen);                                       \
      yystate = *yyssp;                                         \
      goto yybackup;                                            \
    }                                                           \
  else                                                          \
    {                                                           \
      yyerror (YY_("syntax error: cannot back up")); \
      YYERROR;                                                  \
    }                                                           \
while (0)

/* Error token number */
#define YYTERROR        1
#define YYERRCODE       256



/* Enable debugging if requested.  */
#if YYDEBUG

# ifndef YYFPRINTF
#  include <stdio.h> /* INFRINGES ON USER NAME SPACE */
#  define YYFPRINTF fprintf
# endif

# define YYDPRINTF(Args)                        \
do {                                            \
  if (yydebug)                                  \
    YYFPRINTF Args;                             \
} while (0)

/* This macro is provided for backward compatibility. */
#ifndef YY_LOCATION_PRINT
# define YY_LOCATION_PRINT(File, Loc) ((void) 0)
#endif


# define YY_SYMBOL_PRINT(Title, Type, Value, Location)                    \
do {                                                                      \
  if (yydebug)                                                            \
    {                                                                     \
      YYFPRINTF (stderr, "%s ", Title);                                   \
      yy_symbol_print (stderr,                                            \
                  Type, Value); \
      YYFPRINTF (stderr, "\n");                                           \
    }                                                                     \
} while (0)


/*----------------------------------------.
| Print this symbol's value on YYOUTPUT.  |
`----------------------------------------*/

static void
yy_symbol_value_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  FILE *yyo = yyoutput;
  YYUSE (yyo);
  if (!yyvaluep)
    return;
# ifdef YYPRINT
  if (yytype < YYNTOKENS)
    YYPRINT (yyoutput, yytoknum[yytype], *yyvaluep);
# endif
  YYUSE (yytype);
}


/*--------------------------------.
| Print this symbol on YYOUTPUT.  |
`--------------------------------*/

static void
yy_symbol_print (FILE *yyoutput, int yytype, YYSTYPE const * const yyvaluep)
{
  YYFPRINTF (yyoutput, "%s %s (",
             yytype < YYNTOKENS ? "token" : "nterm", yytname[yytype]);

  yy_symbol_value_print (yyoutput, yytype, yyvaluep);
  YYFPRINTF (yyoutput, ")");
}

/*------------------------------------------------------------------.
| yy_stack_print -- Print the state stack from its BOTTOM up to its |
| TOP (included).                                                   |
`------------------------------------------------------------------*/

static void
yy_stack_print (yytype_int16 *yybottom, yytype_int16 *yytop)
{
  YYFPRINTF (stderr, "Stack now");
  for (; yybottom <= yytop; yybottom++)
    {
      int yybot = *yybottom;
      YYFPRINTF (stderr, " %d", yybot);
    }
  YYFPRINTF (stderr, "\n");
}

# define YY_STACK_PRINT(Bottom, Top)                            \
do {                                                            \
  if (yydebug)                                                  \
    yy_stack_print ((Bottom), (Top));                           \
} while (0)


/*------------------------------------------------.
| Report that the YYRULE is going to be reduced.  |
`------------------------------------------------*/

static void
yy_reduce_print (yytype_int16 *yyssp, YYSTYPE *yyvsp, int yyrule)
{
  unsigned long int yylno = yyrline[yyrule];
  int yynrhs = yyr2[yyrule];
  int yyi;
  YYFPRINTF (stderr, "Reducing stack by rule %d (line %lu):\n",
             yyrule - 1, yylno);
  /* The symbols being reduced.  */
  for (yyi = 0; yyi < yynrhs; yyi++)
    {
      YYFPRINTF (stderr, "   $%d = ", yyi + 1);
      yy_symbol_print (stderr,
                       yystos[yyssp[yyi + 1 - yynrhs]],
                       &(yyvsp[(yyi + 1) - (yynrhs)])
                                              );
      YYFPRINTF (stderr, "\n");
    }
}

# define YY_REDUCE_PRINT(Rule)          \
do {                                    \
  if (yydebug)                          \
    yy_reduce_print (yyssp, yyvsp, Rule); \
} while (0)

/* Nonzero means print parse trace.  It is left uninitialized so that
   multiple parsers can coexist.  */
int yydebug;
#else /* !YYDEBUG */
# define YYDPRINTF(Args)
# define YY_SYMBOL_PRINT(Title, Type, Value, Location)
# define YY_STACK_PRINT(Bottom, Top)
# define YY_REDUCE_PRINT(Rule)
#endif /* !YYDEBUG */


/* YYINITDEPTH -- initial size of the parser's stacks.  */
#ifndef YYINITDEPTH
# define YYINITDEPTH 200
#endif

/* YYMAXDEPTH -- maximum size the stacks can grow to (effective only
   if the built-in stack extension method is used).

   Do not make this value too large; the results are undefined if
   YYSTACK_ALLOC_MAXIMUM < YYSTACK_BYTES (YYMAXDEPTH)
   evaluated with infinite-precision integer arithmetic.  */

#ifndef YYMAXDEPTH
# define YYMAXDEPTH 10000
#endif


#if YYERROR_VERBOSE

# ifndef yystrlen
#  if defined __GLIBC__ && defined _STRING_H
#   define yystrlen strlen
#  else
/* Return the length of YYSTR.  */
static YYSIZE_T
yystrlen (const char *yystr)
{
  YYSIZE_T yylen;
  for (yylen = 0; yystr[yylen]; yylen++)
    continue;
  return yylen;
}
#  endif
# endif

# ifndef yystpcpy
#  if defined __GLIBC__ && defined _STRING_H && defined _GNU_SOURCE
#   define yystpcpy stpcpy
#  else
/* Copy YYSRC to YYDEST, returning the address of the terminating '\0' in
   YYDEST.  */
static char *
yystpcpy (char *yydest, const char *yysrc)
{
  char *yyd = yydest;
  const char *yys = yysrc;

  while ((*yyd++ = *yys++) != '\0')
    continue;

  return yyd - 1;
}
#  endif
# endif

# ifndef yytnamerr
/* Copy to YYRES the contents of YYSTR after stripping away unnecessary
   quotes and backslashes, so that it's suitable for yyerror.  The
   heuristic is that double-quoting is unnecessary unless the string
   contains an apostrophe, a comma, or backslash (other than
   backslash-backslash).  YYSTR is taken from yytname.  If YYRES is
   null, do not copy; instead, return the length of what the result
   would have been.  */
static YYSIZE_T
yytnamerr (char *yyres, const char *yystr)
{
  if (*yystr == '"')
    {
      YYSIZE_T yyn = 0;
      char const *yyp = yystr;

      for (;;)
        switch (*++yyp)
          {
          case '\'':
          case ',':
            goto do_not_strip_quotes;

          case '\\':
            if (*++yyp != '\\')
              goto do_not_strip_quotes;
            /* Fall through.  */
          default:
            if (yyres)
              yyres[yyn] = *yyp;
            yyn++;
            break;

          case '"':
            if (yyres)
              yyres[yyn] = '\0';
            return yyn;
          }
    do_not_strip_quotes: ;
    }

  if (! yyres)
    return yystrlen (yystr);

  return yystpcpy (yyres, yystr) - yyres;
}
# endif

/* Copy into *YYMSG, which is of size *YYMSG_ALLOC, an error message
   about the unexpected token YYTOKEN for the state stack whose top is
   YYSSP.

   Return 0 if *YYMSG was successfully written.  Return 1 if *YYMSG is
   not large enough to hold the message.  In that case, also set
   *YYMSG_ALLOC to the required number of bytes.  Return 2 if the
   required number of bytes is too large to store.  */
static int
yysyntax_error (YYSIZE_T *yymsg_alloc, char **yymsg,
                yytype_int16 *yyssp, int yytoken)
{
  YYSIZE_T yysize0 = yytnamerr (YY_NULLPTR, yytname[yytoken]);
  YYSIZE_T yysize = yysize0;
  enum { YYERROR_VERBOSE_ARGS_MAXIMUM = 5 };
  /* Internationalized format string. */
  const char *yyformat = YY_NULLPTR;
  /* Arguments of yyformat. */
  char const *yyarg[YYERROR_VERBOSE_ARGS_MAXIMUM];
  /* Number of reported tokens (one for the "unexpected", one per
     "expected"). */
  int yycount = 0;

  /* There are many possibilities here to consider:
     - If this state is a consistent state with a default action, then
       the only way this function was invoked is if the default action
       is an error action.  In that case, don't check for expected
       tokens because there are none.
     - The only way there can be no lookahead present (in yychar) is if
       this state is a consistent state with a default action.  Thus,
       detecting the absence of a lookahead is sufficient to determine
       that there is no unexpected or expected token to report.  In that
       case, just report a simple "syntax error".
     - Don't assume there isn't a lookahead just because this state is a
       consistent state with a default action.  There might have been a
       previous inconsistent state, consistent state with a non-default
       action, or user semantic action that manipulated yychar.
     - Of course, the expected token list depends on states to have
       correct lookahead information, and it depends on the parser not
       to perform extra reductions after fetching a lookahead from the
       scanner and before detecting a syntax error.  Thus, state merging
       (from LALR or IELR) and default reductions corrupt the expected
       token list.  However, the list is correct for canonical LR with
       one exception: it will still contain any token that will not be
       accepted due to an error action in a later state.
  */
  if (yytoken != YYEMPTY)
    {
      int yyn = yypact[*yyssp];
      yyarg[yycount++] = yytname[yytoken];
      if (!yypact_value_is_default (yyn))
        {
          /* Start YYX at -YYN if negative to avoid negative indexes in
             YYCHECK.  In other words, skip the first -YYN actions for
             this state because they are default actions.  */
          int yyxbegin = yyn < 0 ? -yyn : 0;
          /* Stay within bounds of both yycheck and yytname.  */
          int yychecklim = YYLAST - yyn + 1;
          int yyxend = yychecklim < YYNTOKENS ? yychecklim : YYNTOKENS;
          int yyx;

          for (yyx = yyxbegin; yyx < yyxend; ++yyx)
            if (yycheck[yyx + yyn] == yyx && yyx != YYTERROR
                && !yytable_value_is_error (yytable[yyx + yyn]))
              {
                if (yycount == YYERROR_VERBOSE_ARGS_MAXIMUM)
                  {
                    yycount = 1;
                    yysize = yysize0;
                    break;
                  }
                yyarg[yycount++] = yytname[yyx];
                {
                  YYSIZE_T yysize1 = yysize + yytnamerr (YY_NULLPTR, yytname[yyx]);
                  if (! (yysize <= yysize1
                         && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
                    return 2;
                  yysize = yysize1;
                }
              }
        }
    }

  switch (yycount)
    {
# define YYCASE_(N, S)                      \
      case N:                               \
        yyformat = S;                       \
      break
      YYCASE_(0, YY_("syntax error"));
      YYCASE_(1, YY_("syntax error, unexpected %s"));
      YYCASE_(2, YY_("syntax error, unexpected %s, expecting %s"));
      YYCASE_(3, YY_("syntax error, unexpected %s, expecting %s or %s"));
      YYCASE_(4, YY_("syntax error, unexpected %s, expecting %s or %s or %s"));
      YYCASE_(5, YY_("syntax error, unexpected %s, expecting %s or %s or %s or %s"));
# undef YYCASE_
    }

  {
    YYSIZE_T yysize1 = yysize + yystrlen (yyformat);
    if (! (yysize <= yysize1 && yysize1 <= YYSTACK_ALLOC_MAXIMUM))
      return 2;
    yysize = yysize1;
  }

  if (*yymsg_alloc < yysize)
    {
      *yymsg_alloc = 2 * yysize;
      if (! (yysize <= *yymsg_alloc
             && *yymsg_alloc <= YYSTACK_ALLOC_MAXIMUM))
        *yymsg_alloc = YYSTACK_ALLOC_MAXIMUM;
      return 1;
    }

  /* Avoid sprintf, as that infringes on the user's name space.
     Don't have undefined behavior even if the translation
     produced a string with the wrong number of "%s"s.  */
  {
    char *yyp = *yymsg;
    int yyi = 0;
    while ((*yyp = *yyformat) != '\0')
      if (*yyp == '%' && yyformat[1] == 's' && yyi < yycount)
        {
          yyp += yytnamerr (yyp, yyarg[yyi++]);
          yyformat += 2;
        }
      else
        {
          yyp++;
          yyformat++;
        }
  }
  return 0;
}
#endif /* YYERROR_VERBOSE */

/*-----------------------------------------------.
| Release the memory associated to this symbol.  |
`-----------------------------------------------*/

static void
yydestruct (const char *yymsg, int yytype, YYSTYPE *yyvaluep)
{
  YYUSE (yyvaluep);
  if (!yymsg)
    yymsg = "Deleting";
  YY_SYMBOL_PRINT (yymsg, yytype, yyvaluep, yylocationp);

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  YYUSE (yytype);
  YY_IGNORE_MAYBE_UNINITIALIZED_END
}




/* The lookahead symbol.  */
int yychar;

/* The semantic value of the lookahead symbol.  */
YYSTYPE yylval;
/* Number of syntax errors so far.  */
int yynerrs;


/*----------.
| yyparse.  |
`----------*/

int
yyparse (void)
{
    int yystate;
    /* Number of tokens to shift before error messages enabled.  */
    int yyerrstatus;

    /* The stacks and their tools:
       'yyss': related to states.
       'yyvs': related to semantic values.

       Refer to the stacks through separate pointers, to allow yyoverflow
       to reallocate them elsewhere.  */

    /* The state stack.  */
    yytype_int16 yyssa[YYINITDEPTH];
    yytype_int16 *yyss;
    yytype_int16 *yyssp;

    /* The semantic value stack.  */
    YYSTYPE yyvsa[YYINITDEPTH];
    YYSTYPE *yyvs;
    YYSTYPE *yyvsp;

    YYSIZE_T yystacksize;

  int yyn;
  int yyresult;
  /* Lookahead token as an internal (translated) token number.  */
  int yytoken = 0;
  /* The variables used to return semantic value and location from the
     action routines.  */
  YYSTYPE yyval;

#if YYERROR_VERBOSE
  /* Buffer for error messages, and its allocated size.  */
  char yymsgbuf[128];
  char *yymsg = yymsgbuf;
  YYSIZE_T yymsg_alloc = sizeof yymsgbuf;
#endif

#define YYPOPSTACK(N)   (yyvsp -= (N), yyssp -= (N))

  /* The number of symbols on the RHS of the reduced rule.
     Keep to zero when no symbol should be popped.  */
  int yylen = 0;

  yyssp = yyss = yyssa;
  yyvsp = yyvs = yyvsa;
  yystacksize = YYINITDEPTH;

  YYDPRINTF ((stderr, "Starting parse\n"));

  yystate = 0;
  yyerrstatus = 0;
  yynerrs = 0;
  yychar = YYEMPTY; /* Cause a token to be read.  */
  goto yysetstate;

/*------------------------------------------------------------.
| yynewstate -- Push a new state, which is found in yystate.  |
`------------------------------------------------------------*/
 yynewstate:
  /* In all cases, when you get here, the value and location stacks
     have just been pushed.  So pushing a state here evens the stacks.  */
  yyssp++;

 yysetstate:
  *yyssp = yystate;

  if (yyss + yystacksize - 1 <= yyssp)
    {
      /* Get the current used size of the three stacks, in elements.  */
      YYSIZE_T yysize = yyssp - yyss + 1;

#ifdef yyoverflow
      {
        /* Give user a chance to reallocate the stack.  Use copies of
           these so that the &'s don't force the real ones into
           memory.  */
        YYSTYPE *yyvs1 = yyvs;
        yytype_int16 *yyss1 = yyss;

        /* Each stack pointer address is followed by the size of the
           data in use in that stack, in bytes.  This used to be a
           conditional around just the two extra args, but that might
           be undefined if yyoverflow is a macro.  */
        yyoverflow (YY_("memory exhausted"),
                    &yyss1, yysize * sizeof (*yyssp),
                    &yyvs1, yysize * sizeof (*yyvsp),
                    &yystacksize);

        yyss = yyss1;
        yyvs = yyvs1;
      }
#else /* no yyoverflow */
# ifndef YYSTACK_RELOCATE
      goto yyexhaustedlab;
# else
      /* Extend the stack our own way.  */
      if (YYMAXDEPTH <= yystacksize)
        goto yyexhaustedlab;
      yystacksize *= 2;
      if (YYMAXDEPTH < yystacksize)
        yystacksize = YYMAXDEPTH;

      {
        yytype_int16 *yyss1 = yyss;
        union yyalloc *yyptr =
          (union yyalloc *) YYSTACK_ALLOC (YYSTACK_BYTES (yystacksize));
        if (! yyptr)
          goto yyexhaustedlab;
        YYSTACK_RELOCATE (yyss_alloc, yyss);
        YYSTACK_RELOCATE (yyvs_alloc, yyvs);
#  undef YYSTACK_RELOCATE
        if (yyss1 != yyssa)
          YYSTACK_FREE (yyss1);
      }
# endif
#endif /* no yyoverflow */

      yyssp = yyss + yysize - 1;
      yyvsp = yyvs + yysize - 1;

      YYDPRINTF ((stderr, "Stack size increased to %lu\n",
                  (unsigned long int) yystacksize));

      if (yyss + yystacksize - 1 <= yyssp)
        YYABORT;
    }

  YYDPRINTF ((stderr, "Entering state %d\n", yystate));

  if (yystate == YYFINAL)
    YYACCEPT;

  goto yybackup;

/*-----------.
| yybackup.  |
`-----------*/
yybackup:

  /* Do appropriate processing given the current state.  Read a
     lookahead token if we need one and don't already have one.  */

  /* First try to decide what to do without reference to lookahead token.  */
  yyn = yypact[yystate];
  if (yypact_value_is_default (yyn))
    goto yydefault;

  /* Not known => get a lookahead token if don't already have one.  */

  /* YYCHAR is either YYEMPTY or YYEOF or a valid lookahead symbol.  */
  if (yychar == YYEMPTY)
    {
      YYDPRINTF ((stderr, "Reading a token: "));
      yychar = yylex ();
    }

  if (yychar <= YYEOF)
    {
      yychar = yytoken = YYEOF;
      YYDPRINTF ((stderr, "Now at end of input.\n"));
    }
  else
    {
      yytoken = YYTRANSLATE (yychar);
      YY_SYMBOL_PRINT ("Next token is", yytoken, &yylval, &yylloc);
    }

  /* If the proper action on seeing token YYTOKEN is to reduce or to
     detect an error, take that action.  */
  yyn += yytoken;
  if (yyn < 0 || YYLAST < yyn || yycheck[yyn] != yytoken)
    goto yydefault;
  yyn = yytable[yyn];
  if (yyn <= 0)
    {
      if (yytable_value_is_error (yyn))
        goto yyerrlab;
      yyn = -yyn;
      goto yyreduce;
    }

  /* Count tokens shifted since error; after three, turn off error
     status.  */
  if (yyerrstatus)
    yyerrstatus--;

  /* Shift the lookahead token.  */
  YY_SYMBOL_PRINT ("Shifting", yytoken, &yylval, &yylloc);

  /* Discard the shifted token.  */
  yychar = YYEMPTY;

  yystate = yyn;
  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END

  goto yynewstate;


/*-----------------------------------------------------------.
| yydefault -- do the default action for the current state.  |
`-----------------------------------------------------------*/
yydefault:
  yyn = yydefact[yystate];
  if (yyn == 0)
    goto yyerrlab;
  goto yyreduce;


/*-----------------------------.
| yyreduce -- Do a reduction.  |
`-----------------------------*/
yyreduce:
  /* yyn is the number of a rule to reduce with.  */
  yylen = yyr2[yyn];

  /* If YYLEN is nonzero, implement the default value of the action:
     '$$ = $1'.

     Otherwise, the following line sets YYVAL to garbage.
     This behavior is undocumented and Bison
     users should not rely upon it.  Assigning to YYVAL
     unconditionally makes the parser a bit smaller, and it avoids a
     GCC warning that YYVAL may be used uninitialized.  */
  yyval = yyvsp[1-yylen];


  YY_REDUCE_PRINT (yyn);
  switch (yyn)
    {
        case 19:
#line 175 "slghparse.y" /* yacc.c:1646  */
    { slgh->resetConstructors(); }
#line 2257 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 20:
#line 177 "slghparse.y" /* yacc.c:1646  */
    { slgh->setEndian(1); }
#line 2263 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 21:
#line 178 "slghparse.y" /* yacc.c:1646  */
    { slgh->setEndian(0); }
#line 2269 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 22:
#line 180 "slghparse.y" /* yacc.c:1646  */
    { slgh->setAlignment(*(yyvsp[-1].i)); delete (yyvsp[-1].i); }
#line 2275 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 23:
#line 182 "slghparse.y" /* yacc.c:1646  */
    {}
#line 2281 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 24:
#line 184 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tokensym) = slgh->defineToken((yyvsp[-3].str),(yyvsp[-1].i)); }
#line 2287 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 25:
#line 185 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tokensym) = (yyvsp[-1].tokensym); slgh->addTokenField((yyvsp[-1].tokensym),(yyvsp[0].fieldqual)); }
#line 2293 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 26:
#line 186 "slghparse.y" /* yacc.c:1646  */
    { string errmsg=(yyvsp[0].anysym)->getName()+": redefined as a token"; yyerror(errmsg.c_str()); YYERROR; }
#line 2299 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 27:
#line 188 "slghparse.y" /* yacc.c:1646  */
    {}
#line 2305 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 28:
#line 190 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varsym) = (yyvsp[0].varsym); }
#line 2311 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 29:
#line 191 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varsym) = (yyvsp[-1].varsym); if (!slgh->addContextField( (yyvsp[-1].varsym), (yyvsp[0].fieldqual) ))
                                            { yyerror("All context definitions must come before constructors"); YYERROR; } }
#line 2318 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 30:
#line 194 "slghparse.y" /* yacc.c:1646  */
    { (yyval.fieldqual) = new FieldQuality((yyvsp[-6].str),(yyvsp[-3].i),(yyvsp[-1].i)); }
#line 2324 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 31:
#line 195 "slghparse.y" /* yacc.c:1646  */
    { delete (yyvsp[-3].i); delete (yyvsp[-1].i); string errmsg = (yyvsp[-6].anysym)->getName()+": redefined as field"; yyerror(errmsg.c_str()); YYERROR; }
#line 2330 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 32:
#line 196 "slghparse.y" /* yacc.c:1646  */
    { (yyval.fieldqual) = (yyvsp[-1].fieldqual); (yyval.fieldqual)->signext = true; }
#line 2336 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 33:
#line 197 "slghparse.y" /* yacc.c:1646  */
    { (yyval.fieldqual) = (yyvsp[-1].fieldqual); (yyval.fieldqual)->hex = true; }
#line 2342 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 34:
#line 198 "slghparse.y" /* yacc.c:1646  */
    { (yyval.fieldqual) = (yyvsp[-1].fieldqual); (yyval.fieldqual)->hex = false; }
#line 2348 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 35:
#line 200 "slghparse.y" /* yacc.c:1646  */
    { (yyval.fieldqual) = new FieldQuality((yyvsp[-6].str),(yyvsp[-3].i),(yyvsp[-1].i)); }
#line 2354 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 36:
#line 201 "slghparse.y" /* yacc.c:1646  */
    { delete (yyvsp[-3].i); delete (yyvsp[-1].i); string errmsg = (yyvsp[-6].anysym)->getName()+": redefined as field"; yyerror(errmsg.c_str()); YYERROR; }
#line 2360 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 37:
#line 202 "slghparse.y" /* yacc.c:1646  */
    { (yyval.fieldqual) = (yyvsp[-1].fieldqual); (yyval.fieldqual)->signext = true; }
#line 2366 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 38:
#line 203 "slghparse.y" /* yacc.c:1646  */
    { (yyval.fieldqual) = (yyvsp[-1].fieldqual); (yyval.fieldqual)->flow = false; }
#line 2372 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 39:
#line 204 "slghparse.y" /* yacc.c:1646  */
    { (yyval.fieldqual) = (yyvsp[-1].fieldqual); (yyval.fieldqual)->hex = true; }
#line 2378 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 40:
#line 205 "slghparse.y" /* yacc.c:1646  */
    { (yyval.fieldqual) = (yyvsp[-1].fieldqual); (yyval.fieldqual)->hex = false; }
#line 2384 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 41:
#line 207 "slghparse.y" /* yacc.c:1646  */
    { slgh->newSpace((yyvsp[-1].spacequal)); }
#line 2390 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 42:
#line 209 "slghparse.y" /* yacc.c:1646  */
    { (yyval.spacequal) = new SpaceQuality(*(yyvsp[0].str)); delete (yyvsp[0].str); }
#line 2396 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 43:
#line 210 "slghparse.y" /* yacc.c:1646  */
    { string errmsg = (yyvsp[0].anysym)->getName()+": redefined as space"; yyerror(errmsg.c_str()); YYERROR; }
#line 2402 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 44:
#line 211 "slghparse.y" /* yacc.c:1646  */
    { (yyval.spacequal) = (yyvsp[-3].spacequal); (yyval.spacequal)->type = SpaceQuality::ramtype; }
#line 2408 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 45:
#line 212 "slghparse.y" /* yacc.c:1646  */
    { (yyval.spacequal) = (yyvsp[-3].spacequal); (yyval.spacequal)->type = SpaceQuality::registertype; }
#line 2414 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 46:
#line 213 "slghparse.y" /* yacc.c:1646  */
    { (yyval.spacequal) = (yyvsp[-3].spacequal); (yyval.spacequal)->size = *(yyvsp[0].i); delete (yyvsp[0].i); }
#line 2420 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 47:
#line 214 "slghparse.y" /* yacc.c:1646  */
    { (yyval.spacequal) = (yyvsp[-3].spacequal); (yyval.spacequal)->wordsize = *(yyvsp[0].i); delete (yyvsp[0].i); }
#line 2426 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 48:
#line 215 "slghparse.y" /* yacc.c:1646  */
    { (yyval.spacequal) = (yyvsp[-1].spacequal); (yyval.spacequal)->isdefault = true; }
#line 2432 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 49:
#line 217 "slghparse.y" /* yacc.c:1646  */
    {
               slgh->defineVarnodes((yyvsp[-8].spacesym),(yyvsp[-5].i),(yyvsp[-2].i),(yyvsp[-1].strlist)); }
#line 2439 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 50:
#line 219 "slghparse.y" /* yacc.c:1646  */
    { yyerror("Parsed integer is too big (overflow)"); YYERROR; }
#line 2445 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 54:
#line 226 "slghparse.y" /* yacc.c:1646  */
    {
               slgh->defineBitrange((yyvsp[-7].str),(yyvsp[-5].varsym),(uint4)*(yyvsp[-3].i),(uint4)*(yyvsp[-1].i)); delete (yyvsp[-3].i); delete (yyvsp[-1].i); }
#line 2452 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 55:
#line 229 "slghparse.y" /* yacc.c:1646  */
    { slgh->addUserOp((yyvsp[-1].strlist)); }
#line 2458 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 56:
#line 231 "slghparse.y" /* yacc.c:1646  */
    { slgh->attachValues((yyvsp[-2].symlist),(yyvsp[-1].biglist)); }
#line 2464 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 57:
#line 233 "slghparse.y" /* yacc.c:1646  */
    { slgh->attachNames((yyvsp[-2].symlist),(yyvsp[-1].strlist)); }
#line 2470 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 58:
#line 235 "slghparse.y" /* yacc.c:1646  */
    { slgh->attachVarnodes((yyvsp[-2].symlist),(yyvsp[-1].symlist)); }
#line 2476 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 59:
#line 237 "slghparse.y" /* yacc.c:1646  */
    { slgh->buildMacro((yyvsp[-3].macrosym),(yyvsp[-1].sem)); }
#line 2482 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 60:
#line 240 "slghparse.y" /* yacc.c:1646  */
    {  slgh->pushWith((yyvsp[-4].subtablesym),(yyvsp[-2].pateq),(yyvsp[-1].contop)); }
#line 2488 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 64:
#line 246 "slghparse.y" /* yacc.c:1646  */
    { slgh->popWith(); }
#line 2494 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 65:
#line 248 "slghparse.y" /* yacc.c:1646  */
    { (yyval.subtablesym) = (SubtableSymbol *)0; }
#line 2500 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 66:
#line 249 "slghparse.y" /* yacc.c:1646  */
    { (yyval.subtablesym) = (yyvsp[0].subtablesym); }
#line 2506 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 67:
#line 250 "slghparse.y" /* yacc.c:1646  */
    { (yyval.subtablesym) = slgh->newTable((yyvsp[0].str)); }
#line 2512 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 68:
#line 253 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = (PatternEquation *)0; }
#line 2518 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 69:
#line 254 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = (yyvsp[0].pateq); }
#line 2524 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 70:
#line 257 "slghparse.y" /* yacc.c:1646  */
    { (yyval.macrosym) = slgh->createMacro((yyvsp[-3].str),(yyvsp[-1].strlist)); }
#line 2530 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 71:
#line 259 "slghparse.y" /* yacc.c:1646  */
    { (yyval.sectionstart) = slgh->standaloneSection((yyvsp[-1].sem)); }
#line 2536 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 72:
#line 260 "slghparse.y" /* yacc.c:1646  */
    { (yyval.sectionstart) = slgh->finalNamedSection((yyvsp[-2].sectionstart),(yyvsp[-1].sem)); }
#line 2542 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 73:
#line 261 "slghparse.y" /* yacc.c:1646  */
    { (yyval.sectionstart) = (SectionVector *)0; }
#line 2548 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 74:
#line 263 "slghparse.y" /* yacc.c:1646  */
    { slgh->buildConstructor((yyvsp[-4].construct),(yyvsp[-2].pateq),(yyvsp[-1].contop),(yyvsp[0].sectionstart)); }
#line 2554 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 75:
#line 264 "slghparse.y" /* yacc.c:1646  */
    { slgh->buildConstructor((yyvsp[-4].construct),(yyvsp[-2].pateq),(yyvsp[-1].contop),(yyvsp[0].sectionstart)); }
#line 2560 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 76:
#line 266 "slghparse.y" /* yacc.c:1646  */
    { (yyval.construct) = (yyvsp[-1].construct); (yyval.construct)->addSyntax(*(yyvsp[0].str)); delete (yyvsp[0].str); }
#line 2566 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 77:
#line 267 "slghparse.y" /* yacc.c:1646  */
    { (yyval.construct) = (yyvsp[-1].construct); (yyval.construct)->addSyntax(*(yyvsp[0].str)); delete (yyvsp[0].str); }
#line 2572 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 78:
#line 268 "slghparse.y" /* yacc.c:1646  */
    { (yyval.construct) = (yyvsp[-1].construct); if (slgh->isInRoot((yyvsp[-1].construct))) { (yyval.construct)->addSyntax(*(yyvsp[0].str)); delete (yyvsp[0].str); } else slgh->newOperand((yyvsp[-1].construct),(yyvsp[0].str)); }
#line 2578 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 79:
#line 269 "slghparse.y" /* yacc.c:1646  */
    { (yyval.construct) = (yyvsp[-1].construct); if (!slgh->isInRoot((yyvsp[-1].construct))) { yyerror("Unexpected '^' at start of print pieces");  YYERROR; } }
#line 2584 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 80:
#line 270 "slghparse.y" /* yacc.c:1646  */
    { (yyval.construct) = (yyvsp[-1].construct); }
#line 2590 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 81:
#line 271 "slghparse.y" /* yacc.c:1646  */
    { (yyval.construct) = (yyvsp[-1].construct); (yyval.construct)->addSyntax(*(yyvsp[0].str)); delete (yyvsp[0].str); }
#line 2596 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 82:
#line 272 "slghparse.y" /* yacc.c:1646  */
    { (yyval.construct) = (yyvsp[-1].construct); (yyval.construct)->addSyntax(*(yyvsp[0].str)); delete (yyvsp[0].str); }
#line 2602 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 83:
#line 273 "slghparse.y" /* yacc.c:1646  */
    { (yyval.construct) = (yyvsp[-1].construct); (yyval.construct)->addSyntax(string(" ")); }
#line 2608 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 84:
#line 274 "slghparse.y" /* yacc.c:1646  */
    { (yyval.construct) = (yyvsp[-1].construct); slgh->newOperand((yyvsp[-1].construct),(yyvsp[0].str)); }
#line 2614 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 85:
#line 276 "slghparse.y" /* yacc.c:1646  */
    { (yyval.construct) = slgh->createConstructor((yyvsp[-1].subtablesym)); }
#line 2620 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 86:
#line 277 "slghparse.y" /* yacc.c:1646  */
    { SubtableSymbol *sym=slgh->newTable((yyvsp[-1].str)); (yyval.construct) = slgh->createConstructor(sym); }
#line 2626 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 87:
#line 278 "slghparse.y" /* yacc.c:1646  */
    { (yyval.construct) = slgh->createConstructor((SubtableSymbol *)0); }
#line 2632 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 88:
#line 279 "slghparse.y" /* yacc.c:1646  */
    { (yyval.construct) = (yyvsp[-1].construct); }
#line 2638 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 89:
#line 281 "slghparse.y" /* yacc.c:1646  */
    { (yyval.patexp) = new ConstantValue(*(yyvsp[0].big)); delete (yyvsp[0].big); }
#line 2644 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 90:
#line 283 "slghparse.y" /* yacc.c:1646  */
    { if ((actionon==1)&&((yyvsp[0].famsym)->getType() != SleighSymbol::context_symbol))
                                             { string errmsg="Global symbol "+(yyvsp[0].famsym)->getName(); errmsg += " is not allowed in action expression"; yyerror(errmsg.c_str()); } (yyval.patexp) = (yyvsp[0].famsym)->getPatternValue(); }
#line 2651 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 91:
#line 286 "slghparse.y" /* yacc.c:1646  */
    { (yyval.patexp) = (yyvsp[0].specsym)->getPatternExpression(); }
#line 2657 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 92:
#line 287 "slghparse.y" /* yacc.c:1646  */
    { (yyval.patexp) = (yyvsp[-1].patexp); }
#line 2663 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 93:
#line 288 "slghparse.y" /* yacc.c:1646  */
    { (yyval.patexp) = new PlusExpression((yyvsp[-2].patexp),(yyvsp[0].patexp)); }
#line 2669 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 94:
#line 289 "slghparse.y" /* yacc.c:1646  */
    { (yyval.patexp) = new SubExpression((yyvsp[-2].patexp),(yyvsp[0].patexp)); }
#line 2675 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 95:
#line 290 "slghparse.y" /* yacc.c:1646  */
    { (yyval.patexp) = new MultExpression((yyvsp[-2].patexp),(yyvsp[0].patexp)); }
#line 2681 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 96:
#line 291 "slghparse.y" /* yacc.c:1646  */
    { (yyval.patexp) = new LeftShiftExpression((yyvsp[-2].patexp),(yyvsp[0].patexp)); }
#line 2687 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 97:
#line 292 "slghparse.y" /* yacc.c:1646  */
    { (yyval.patexp) = new RightShiftExpression((yyvsp[-2].patexp),(yyvsp[0].patexp)); }
#line 2693 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 98:
#line 293 "slghparse.y" /* yacc.c:1646  */
    { (yyval.patexp) = new AndExpression((yyvsp[-2].patexp),(yyvsp[0].patexp)); }
#line 2699 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 99:
#line 294 "slghparse.y" /* yacc.c:1646  */
    { (yyval.patexp) = new OrExpression((yyvsp[-2].patexp),(yyvsp[0].patexp)); }
#line 2705 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 100:
#line 295 "slghparse.y" /* yacc.c:1646  */
    { (yyval.patexp) = new XorExpression((yyvsp[-2].patexp),(yyvsp[0].patexp)); }
#line 2711 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 101:
#line 296 "slghparse.y" /* yacc.c:1646  */
    { (yyval.patexp) = new DivExpression((yyvsp[-2].patexp),(yyvsp[0].patexp)); }
#line 2717 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 102:
#line 297 "slghparse.y" /* yacc.c:1646  */
    { (yyval.patexp) = new MinusExpression((yyvsp[0].patexp)); }
#line 2723 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 103:
#line 298 "slghparse.y" /* yacc.c:1646  */
    { (yyval.patexp) = new NotExpression((yyvsp[0].patexp)); }
#line 2729 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 105:
#line 301 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = new EquationAnd((yyvsp[-2].pateq),(yyvsp[0].pateq)); }
#line 2735 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 106:
#line 302 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = new EquationOr((yyvsp[-2].pateq),(yyvsp[0].pateq)); }
#line 2741 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 107:
#line 303 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = new EquationCat((yyvsp[-2].pateq),(yyvsp[0].pateq)); }
#line 2747 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 108:
#line 305 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = new EquationLeftEllipsis((yyvsp[0].pateq)); }
#line 2753 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 110:
#line 308 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = new EquationRightEllipsis((yyvsp[-1].pateq)); }
#line 2759 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 113:
#line 312 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = (yyvsp[-1].pateq); }
#line 2765 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 114:
#line 314 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = new EqualEquation((yyvsp[-2].famsym)->getPatternValue(),(yyvsp[0].patexp)); }
#line 2771 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 115:
#line 315 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = new NotEqualEquation((yyvsp[-2].famsym)->getPatternValue(),(yyvsp[0].patexp)); }
#line 2777 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 116:
#line 316 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = new LessEquation((yyvsp[-2].famsym)->getPatternValue(),(yyvsp[0].patexp)); }
#line 2783 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 117:
#line 317 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = new LessEqualEquation((yyvsp[-2].famsym)->getPatternValue(),(yyvsp[0].patexp)); }
#line 2789 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 118:
#line 318 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = new GreaterEquation((yyvsp[-2].famsym)->getPatternValue(),(yyvsp[0].patexp)); }
#line 2795 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 119:
#line 319 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = new GreaterEqualEquation((yyvsp[-2].famsym)->getPatternValue(),(yyvsp[0].patexp)); }
#line 2801 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 120:
#line 320 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = slgh->constrainOperand((yyvsp[-2].operandsym),(yyvsp[0].patexp)); 
                                          if ((yyval.pateq) == (PatternEquation *)0) 
                                            { string errmsg="Constraining currently undefined operand "+(yyvsp[-2].operandsym)->getName(); yyerror(errmsg.c_str()); } }
#line 2809 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 121:
#line 323 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = new OperandEquation((yyvsp[0].operandsym)->getIndex()); slgh->selfDefine((yyvsp[0].operandsym)); }
#line 2815 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 122:
#line 324 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = new UnconstrainedEquation((yyvsp[0].specsym)->getPatternExpression()); }
#line 2821 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 123:
#line 325 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = slgh->defineInvisibleOperand((yyvsp[0].famsym)); }
#line 2827 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 124:
#line 326 "slghparse.y" /* yacc.c:1646  */
    { (yyval.pateq) = slgh->defineInvisibleOperand((yyvsp[0].subtablesym)); }
#line 2833 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 125:
#line 328 "slghparse.y" /* yacc.c:1646  */
    { (yyval.contop) = (vector<ContextChange *> *)0; }
#line 2839 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 126:
#line 329 "slghparse.y" /* yacc.c:1646  */
    { (yyval.contop) = (yyvsp[-1].contop); }
#line 2845 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 127:
#line 331 "slghparse.y" /* yacc.c:1646  */
    { (yyval.contop) = new vector<ContextChange *>; }
#line 2851 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 128:
#line 332 "slghparse.y" /* yacc.c:1646  */
    { (yyval.contop) = (yyvsp[-4].contop); if (!slgh->contextMod((yyvsp[-4].contop),(yyvsp[-3].contextsym),(yyvsp[-1].patexp))) { string errmsg="Cannot use 'inst_next' to set context variable: "+(yyvsp[-3].contextsym)->getName(); yyerror(errmsg.c_str()); YYERROR; } }
#line 2857 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 129:
#line 333 "slghparse.y" /* yacc.c:1646  */
    { (yyval.contop) = (yyvsp[-7].contop); slgh->contextSet((yyvsp[-7].contop),(yyvsp[-4].famsym),(yyvsp[-2].contextsym)); }
#line 2863 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 130:
#line 334 "slghparse.y" /* yacc.c:1646  */
    { (yyval.contop) = (yyvsp[-7].contop); slgh->contextSet((yyvsp[-7].contop),(yyvsp[-4].specsym),(yyvsp[-2].contextsym)); }
#line 2869 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 131:
#line 335 "slghparse.y" /* yacc.c:1646  */
    { (yyval.contop) = (yyvsp[-4].contop); slgh->defineOperand((yyvsp[-3].operandsym),(yyvsp[-1].patexp)); }
#line 2875 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 132:
#line 336 "slghparse.y" /* yacc.c:1646  */
    { string errmsg="Expecting context symbol, not "+*(yyvsp[0].str); delete (yyvsp[0].str); yyerror(errmsg.c_str()); YYERROR; }
#line 2881 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 133:
#line 338 "slghparse.y" /* yacc.c:1646  */
    { (yyval.sectionsym) = slgh->newSectionSymbol( *(yyvsp[-1].str) ); delete (yyvsp[-1].str); }
#line 2887 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 134:
#line 339 "slghparse.y" /* yacc.c:1646  */
    { (yyval.sectionsym) = (yyvsp[-1].sectionsym); }
#line 2893 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 135:
#line 341 "slghparse.y" /* yacc.c:1646  */
    { (yyval.sectionstart) = slgh->firstNamedSection((yyvsp[-1].sem),(yyvsp[0].sectionsym)); }
#line 2899 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 136:
#line 343 "slghparse.y" /* yacc.c:1646  */
    { (yyval.sectionstart) = (yyvsp[0].sectionstart); }
#line 2905 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 137:
#line 344 "slghparse.y" /* yacc.c:1646  */
    { (yyval.sectionstart) = slgh->nextNamedSection((yyvsp[-2].sectionstart),(yyvsp[-1].sem),(yyvsp[0].sectionsym)); }
#line 2911 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 138:
#line 346 "slghparse.y" /* yacc.c:1646  */
    { (yyval.sem) = (yyvsp[0].sem); if ((yyval.sem)->getOpvec().empty() && ((yyval.sem)->getResult() == (HandleTpl *)0)) slgh->recordNop(); }
#line 2917 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 139:
#line 347 "slghparse.y" /* yacc.c:1646  */
    { (yyval.sem) = slgh->setResultVarnode((yyvsp[-3].sem),(yyvsp[-1].varnode)); }
#line 2923 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 140:
#line 348 "slghparse.y" /* yacc.c:1646  */
    { (yyval.sem) = slgh->setResultStarVarnode((yyvsp[-4].sem),(yyvsp[-2].starqual),(yyvsp[-1].varnode)); }
#line 2929 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 141:
#line 349 "slghparse.y" /* yacc.c:1646  */
    { string errmsg="Unknown export varnode: "+*(yyvsp[0].str); delete (yyvsp[0].str); yyerror(errmsg.c_str()); YYERROR; }
#line 2935 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 142:
#line 350 "slghparse.y" /* yacc.c:1646  */
    { string errmsg="Unknown pointer varnode: "+*(yyvsp[0].str); delete (yyvsp[-1].starqual); delete (yyvsp[0].str); yyerror(errmsg.c_str()); YYERROR; }
#line 2941 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 143:
#line 352 "slghparse.y" /* yacc.c:1646  */
    { (yyval.sem) = new ConstructTpl(); }
#line 2947 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 144:
#line 353 "slghparse.y" /* yacc.c:1646  */
    { (yyval.sem) = (yyvsp[-1].sem); if (!(yyval.sem)->addOpList(*(yyvsp[0].stmt))) { delete (yyvsp[0].stmt); yyerror("Multiple delayslot declarations"); YYERROR; } delete (yyvsp[0].stmt); }
#line 2953 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 145:
#line 354 "slghparse.y" /* yacc.c:1646  */
    { (yyval.sem) = (yyvsp[-3].sem); slgh->pcode.newLocalDefinition((yyvsp[-1].str)); }
#line 2959 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 146:
#line 355 "slghparse.y" /* yacc.c:1646  */
    { (yyval.sem) = (yyvsp[-5].sem); slgh->pcode.newLocalDefinition((yyvsp[-3].str),*(yyvsp[-1].i)); delete (yyvsp[-1].i); }
#line 2965 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 147:
#line 357 "slghparse.y" /* yacc.c:1646  */
    { (yyvsp[-1].tree)->setOutput((yyvsp[-3].varnode)); (yyval.stmt) = ExprTree::toVector((yyvsp[-1].tree)); }
#line 2971 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 148:
#line 358 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->pcode.newOutput(true,(yyvsp[-1].tree),(yyvsp[-3].str)); }
#line 2977 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 149:
#line 359 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->pcode.newOutput(false,(yyvsp[-1].tree),(yyvsp[-3].str)); }
#line 2983 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 150:
#line 360 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->pcode.newOutput(true,(yyvsp[-1].tree),(yyvsp[-5].str),*(yyvsp[-3].i)); delete (yyvsp[-3].i); }
#line 2989 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 151:
#line 361 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->pcode.newOutput(true,(yyvsp[-1].tree),(yyvsp[-5].str),*(yyvsp[-3].i)); delete (yyvsp[-3].i); }
#line 2995 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 152:
#line 362 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = (vector<OpTpl *> *)0; string errmsg = "Redefinition of symbol: "+(yyvsp[-1].specsym)->getName(); yyerror(errmsg.c_str()); YYERROR; }
#line 3001 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 153:
#line 363 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->pcode.createStore((yyvsp[-4].starqual),(yyvsp[-3].tree),(yyvsp[-1].tree)); }
#line 3007 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 154:
#line 364 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->pcode.createUserOpNoOut((yyvsp[-4].useropsym),(yyvsp[-2].param)); }
#line 3013 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 155:
#line 365 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->pcode.assignBitRange((yyvsp[-8].varnode),(uint4)*(yyvsp[-6].i),(uint4)*(yyvsp[-4].i),(yyvsp[-1].tree)); delete (yyvsp[-6].i), delete (yyvsp[-4].i); }
#line 3019 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 156:
#line 366 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt)=slgh->pcode.assignBitRange((yyvsp[-3].bitsym)->getParentSymbol()->getVarnode(),(yyvsp[-3].bitsym)->getBitOffset(),(yyvsp[-3].bitsym)->numBits(),(yyvsp[-1].tree)); }
#line 3025 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 157:
#line 367 "slghparse.y" /* yacc.c:1646  */
    { delete (yyvsp[-3].varnode); delete (yyvsp[-1].i); yyerror("Illegal truncation on left-hand side of assignment"); YYERROR; }
#line 3031 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 158:
#line 368 "slghparse.y" /* yacc.c:1646  */
    { delete (yyvsp[-3].varnode); delete (yyvsp[-1].i); yyerror("Illegal subpiece on left-hand side of assignment"); YYERROR; }
#line 3037 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 159:
#line 369 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->pcode.createOpConst(BUILD,(yyvsp[-1].operandsym)->getIndex()); }
#line 3043 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 160:
#line 370 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->createCrossBuild((yyvsp[-3].varnode),(yyvsp[-1].sectionsym)); }
#line 3049 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 161:
#line 371 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->createCrossBuild((yyvsp[-3].varnode),slgh->newSectionSymbol(*(yyvsp[-1].str))); delete (yyvsp[-1].str); }
#line 3055 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 162:
#line 372 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->pcode.createOpConst(DELAY_SLOT,*(yyvsp[-2].i)); delete (yyvsp[-2].i); }
#line 3061 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 163:
#line 373 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->pcode.createOpNoOut(CPUI_BRANCH,new ExprTree((yyvsp[-1].varnode))); }
#line 3067 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 164:
#line 374 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->pcode.createOpNoOut(CPUI_CBRANCH,new ExprTree((yyvsp[-1].varnode)),(yyvsp[-3].tree)); }
#line 3073 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 165:
#line 375 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->pcode.createOpNoOut(CPUI_BRANCHIND,(yyvsp[-2].tree)); }
#line 3079 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 166:
#line 376 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->pcode.createOpNoOut(CPUI_CALL,new ExprTree((yyvsp[-1].varnode))); }
#line 3085 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 167:
#line 377 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->pcode.createOpNoOut(CPUI_CALLIND,(yyvsp[-2].tree)); }
#line 3091 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 168:
#line 378 "slghparse.y" /* yacc.c:1646  */
    { yyerror("Must specify an indirect parameter for return"); YYERROR; }
#line 3097 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 169:
#line 379 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->pcode.createOpNoOut(CPUI_RETURN,(yyvsp[-2].tree)); }
#line 3103 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 170:
#line 380 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->createMacroUse((yyvsp[-4].macrosym),(yyvsp[-2].param)); }
#line 3109 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 171:
#line 381 "slghparse.y" /* yacc.c:1646  */
    { (yyval.stmt) = slgh->pcode.placeLabel( (yyvsp[0].labelsym) ); }
#line 3115 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 172:
#line 383 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = new ExprTree((yyvsp[0].varnode)); }
#line 3121 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 173:
#line 384 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createLoad((yyvsp[-1].starqual),(yyvsp[0].tree)); }
#line 3127 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 174:
#line 385 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = (yyvsp[-1].tree); }
#line 3133 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 175:
#line 386 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_ADD,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3139 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 176:
#line 387 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_SUB,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3145 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 177:
#line 388 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_EQUAL,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3151 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 178:
#line 389 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_NOTEQUAL,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3157 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 179:
#line 390 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_LESS,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3163 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 180:
#line 391 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_LESSEQUAL,(yyvsp[0].tree),(yyvsp[-2].tree)); }
#line 3169 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 181:
#line 392 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_LESSEQUAL,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3175 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 182:
#line 393 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_LESS,(yyvsp[0].tree),(yyvsp[-2].tree)); }
#line 3181 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 183:
#line 394 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_SLESS,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3187 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 184:
#line 395 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_SLESSEQUAL,(yyvsp[0].tree),(yyvsp[-2].tree)); }
#line 3193 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 185:
#line 396 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_SLESSEQUAL,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3199 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 186:
#line 397 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_SLESS,(yyvsp[0].tree),(yyvsp[-2].tree)); }
#line 3205 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 187:
#line 398 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_2COMP,(yyvsp[0].tree)); }
#line 3211 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 188:
#line 399 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_NEGATE,(yyvsp[0].tree)); }
#line 3217 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 189:
#line 400 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_XOR,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3223 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 190:
#line 401 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_AND,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3229 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 191:
#line 402 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_OR,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3235 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 192:
#line 403 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_LEFT,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3241 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 193:
#line 404 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_RIGHT,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3247 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 194:
#line 405 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_SRIGHT,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3253 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 195:
#line 406 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_MULT,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3259 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 196:
#line 407 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_DIV,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3265 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 197:
#line 408 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_SDIV,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3271 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 198:
#line 409 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_REM,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3277 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 199:
#line 410 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_SREM,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3283 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 200:
#line 411 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_BOOL_NEGATE,(yyvsp[0].tree)); }
#line 3289 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 201:
#line 412 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_BOOL_XOR,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3295 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 202:
#line 413 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_BOOL_AND,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3301 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 203:
#line 414 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_BOOL_OR,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3307 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 204:
#line 415 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_EQUAL,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3313 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 205:
#line 416 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_NOTEQUAL,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3319 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 206:
#line 417 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_LESS,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3325 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 207:
#line 418 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_LESS,(yyvsp[0].tree),(yyvsp[-2].tree)); }
#line 3331 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 208:
#line 419 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_LESSEQUAL,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3337 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 209:
#line 420 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_LESSEQUAL,(yyvsp[0].tree),(yyvsp[-2].tree)); }
#line 3343 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 210:
#line 421 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_ADD,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3349 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 211:
#line 422 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_SUB,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3355 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 212:
#line 423 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_MULT,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3361 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 213:
#line 424 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_DIV,(yyvsp[-2].tree),(yyvsp[0].tree)); }
#line 3367 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 214:
#line 425 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_NEG,(yyvsp[0].tree)); }
#line 3373 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 215:
#line 426 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_ABS,(yyvsp[-1].tree)); }
#line 3379 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 216:
#line 427 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_SQRT,(yyvsp[-1].tree)); }
#line 3385 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 217:
#line 428 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_SEXT,(yyvsp[-1].tree)); }
#line 3391 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 218:
#line 429 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_ZEXT,(yyvsp[-1].tree)); }
#line 3397 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 219:
#line 430 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_CARRY,(yyvsp[-3].tree),(yyvsp[-1].tree)); }
#line 3403 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 220:
#line 431 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_SCARRY,(yyvsp[-3].tree),(yyvsp[-1].tree)); }
#line 3409 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 221:
#line 432 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_INT_SBORROW,(yyvsp[-3].tree),(yyvsp[-1].tree)); }
#line 3415 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 222:
#line 433 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_FLOAT2FLOAT,(yyvsp[-1].tree)); }
#line 3421 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 223:
#line 434 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_INT2FLOAT,(yyvsp[-1].tree)); }
#line 3427 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 224:
#line 435 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_NAN,(yyvsp[-1].tree)); }
#line 3433 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 225:
#line 436 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_TRUNC,(yyvsp[-1].tree)); }
#line 3439 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 226:
#line 437 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_CEIL,(yyvsp[-1].tree)); }
#line 3445 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 227:
#line 438 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_FLOOR,(yyvsp[-1].tree)); }
#line 3451 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 228:
#line 439 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_FLOAT_ROUND,(yyvsp[-1].tree)); }
#line 3457 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 229:
#line 440 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_NEW,(yyvsp[-1].tree)); }
#line 3463 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 230:
#line 441 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_NEW,(yyvsp[-3].tree),(yyvsp[-1].tree)); }
#line 3469 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 231:
#line 442 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_POPCOUNT,(yyvsp[-1].tree)); }
#line 3475 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 232:
#line 443 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createOp(CPUI_SUBPIECE,new ExprTree((yyvsp[-3].specsym)->getVarnode()),new ExprTree((yyvsp[-1].varnode))); }
#line 3481 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 233:
#line 444 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createBitRange((yyvsp[-2].specsym),0,(uint4)(*(yyvsp[0].i) * 8)); delete (yyvsp[0].i); }
#line 3487 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 234:
#line 445 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createBitRange((yyvsp[-5].specsym),(uint4)*(yyvsp[-3].i),(uint4)*(yyvsp[-1].i)); delete (yyvsp[-3].i), delete (yyvsp[-1].i); }
#line 3493 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 235:
#line 446 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree)=slgh->pcode.createBitRange((yyvsp[0].bitsym)->getParentSymbol(),(yyvsp[0].bitsym)->getBitOffset(),(yyvsp[0].bitsym)->numBits()); }
#line 3499 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 236:
#line 447 "slghparse.y" /* yacc.c:1646  */
    { (yyval.tree) = slgh->pcode.createUserOp((yyvsp[-3].useropsym),(yyvsp[-1].param)); }
#line 3505 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 237:
#line 448 "slghparse.y" /* yacc.c:1646  */
    { if ((*(yyvsp[-1].param)).size() < 2) { string errmsg = "Must at least two inputs to cpool"; yyerror(errmsg.c_str()); YYERROR; } (yyval.tree) = slgh->pcode.createVariadic(CPUI_CPOOLREF,(yyvsp[-1].param)); }
#line 3511 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 238:
#line 450 "slghparse.y" /* yacc.c:1646  */
    { (yyval.starqual) = new StarQuality; (yyval.starqual)->size = *(yyvsp[0].i); delete (yyvsp[0].i); (yyval.starqual)->id=ConstTpl((yyvsp[-3].spacesym)->getSpace()); }
#line 3517 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 239:
#line 451 "slghparse.y" /* yacc.c:1646  */
    { (yyval.starqual) = new StarQuality; (yyval.starqual)->size = 0; (yyval.starqual)->id=ConstTpl((yyvsp[-1].spacesym)->getSpace()); }
#line 3523 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 240:
#line 452 "slghparse.y" /* yacc.c:1646  */
    { (yyval.starqual) = new StarQuality; (yyval.starqual)->size = *(yyvsp[0].i); delete (yyvsp[0].i); (yyval.starqual)->id=ConstTpl(slgh->getDefaultSpace()); }
#line 3529 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 241:
#line 453 "slghparse.y" /* yacc.c:1646  */
    { (yyval.starqual) = new StarQuality; (yyval.starqual)->size = 0; (yyval.starqual)->id=ConstTpl(slgh->getDefaultSpace()); }
#line 3535 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 242:
#line 455 "slghparse.y" /* yacc.c:1646  */
    { VarnodeTpl *sym = (yyvsp[0].startsym)->getVarnode(); (yyval.varnode) = new VarnodeTpl(ConstTpl(ConstTpl::j_curspace),sym->getOffset(),ConstTpl(ConstTpl::j_curspace_size)); delete sym; }
#line 3541 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 243:
#line 456 "slghparse.y" /* yacc.c:1646  */
    { VarnodeTpl *sym = (yyvsp[0].endsym)->getVarnode(); (yyval.varnode) = new VarnodeTpl(ConstTpl(ConstTpl::j_curspace),sym->getOffset(),ConstTpl(ConstTpl::j_curspace_size)); delete sym; }
#line 3547 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 244:
#line 457 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varnode) = new VarnodeTpl(ConstTpl(ConstTpl::j_curspace),ConstTpl(ConstTpl::real,*(yyvsp[0].i)),ConstTpl(ConstTpl::j_curspace_size)); delete (yyvsp[0].i); }
#line 3553 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 245:
#line 458 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varnode) = new VarnodeTpl(ConstTpl(ConstTpl::j_curspace),ConstTpl(ConstTpl::real,0),ConstTpl(ConstTpl::j_curspace_size)); yyerror("Parsed integer is too big (overflow)"); }
#line 3559 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 246:
#line 459 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varnode) = (yyvsp[0].operandsym)->getVarnode(); (yyvsp[0].operandsym)->setCodeAddress(); }
#line 3565 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 247:
#line 460 "slghparse.y" /* yacc.c:1646  */
    { AddrSpace *spc = (yyvsp[-1].spacesym)->getSpace(); (yyval.varnode) = new VarnodeTpl(ConstTpl(spc),ConstTpl(ConstTpl::real,*(yyvsp[-3].i)),ConstTpl(ConstTpl::real,spc->getAddrSize())); delete (yyvsp[-3].i); }
#line 3571 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 248:
#line 461 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varnode) = new VarnodeTpl(ConstTpl(slgh->getConstantSpace()),ConstTpl(ConstTpl::j_relative,(yyvsp[0].labelsym)->getIndex()),ConstTpl(ConstTpl::real,sizeof(uintm))); (yyvsp[0].labelsym)->incrementRefCount(); }
#line 3577 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 249:
#line 462 "slghparse.y" /* yacc.c:1646  */
    { string errmsg = "Unknown jump destination: "+*(yyvsp[0].str); delete (yyvsp[0].str); yyerror(errmsg.c_str()); YYERROR; }
#line 3583 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 250:
#line 464 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varnode) = (yyvsp[0].specsym)->getVarnode(); }
#line 3589 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 251:
#line 465 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varnode) = (yyvsp[0].varnode); }
#line 3595 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 252:
#line 466 "slghparse.y" /* yacc.c:1646  */
    { string errmsg = "Unknown varnode parameter: "+*(yyvsp[0].str); delete (yyvsp[0].str); yyerror(errmsg.c_str()); YYERROR; }
#line 3601 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 253:
#line 467 "slghparse.y" /* yacc.c:1646  */
    { string errmsg = "Subtable not attached to operand: "+(yyvsp[0].subtablesym)->getName(); yyerror(errmsg.c_str()); YYERROR; }
#line 3607 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 254:
#line 469 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varnode) = new VarnodeTpl(ConstTpl(slgh->getConstantSpace()),ConstTpl(ConstTpl::real,*(yyvsp[0].i)),ConstTpl(ConstTpl::real,0)); delete (yyvsp[0].i); }
#line 3613 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 255:
#line 470 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varnode) = new VarnodeTpl(ConstTpl(slgh->getConstantSpace()),ConstTpl(ConstTpl::real,0),ConstTpl(ConstTpl::real,0)); yyerror("Parsed integer is too big (overflow)"); }
#line 3619 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 256:
#line 471 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varnode) = new VarnodeTpl(ConstTpl(slgh->getConstantSpace()),ConstTpl(ConstTpl::real,*(yyvsp[-2].i)),ConstTpl(ConstTpl::real,*(yyvsp[0].i))); delete (yyvsp[-2].i); delete (yyvsp[0].i); }
#line 3625 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 257:
#line 472 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varnode) = slgh->pcode.addressOf((yyvsp[0].varnode),0); }
#line 3631 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 258:
#line 473 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varnode) = slgh->pcode.addressOf((yyvsp[0].varnode),*(yyvsp[-1].i)); delete (yyvsp[-1].i); }
#line 3637 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 259:
#line 475 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varnode) = (yyvsp[0].specsym)->getVarnode(); }
#line 3643 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 260:
#line 476 "slghparse.y" /* yacc.c:1646  */
    { string errmsg = "Unknown assignment varnode: "+*(yyvsp[0].str); delete (yyvsp[0].str); yyerror(errmsg.c_str()); YYERROR; }
#line 3649 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 261:
#line 477 "slghparse.y" /* yacc.c:1646  */
    { string errmsg = "Subtable not attached to operand: "+(yyvsp[0].subtablesym)->getName(); yyerror(errmsg.c_str()); YYERROR; }
#line 3655 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 262:
#line 479 "slghparse.y" /* yacc.c:1646  */
    { (yyval.labelsym) = (yyvsp[-1].labelsym); }
#line 3661 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 263:
#line 480 "slghparse.y" /* yacc.c:1646  */
    { (yyval.labelsym) = slgh->pcode.defineLabel( (yyvsp[-1].str) ); }
#line 3667 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 264:
#line 482 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varnode) = (yyvsp[0].specsym)->getVarnode(); }
#line 3673 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 265:
#line 483 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varnode) = slgh->pcode.addressOf((yyvsp[0].varnode),0); }
#line 3679 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 266:
#line 484 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varnode) = slgh->pcode.addressOf((yyvsp[0].varnode),*(yyvsp[-1].i)); delete (yyvsp[-1].i); }
#line 3685 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 267:
#line 485 "slghparse.y" /* yacc.c:1646  */
    { (yyval.varnode) = new VarnodeTpl(ConstTpl(slgh->getConstantSpace()),ConstTpl(ConstTpl::real,*(yyvsp[-2].i)),ConstTpl(ConstTpl::real,*(yyvsp[0].i))); delete (yyvsp[-2].i); delete (yyvsp[0].i); }
#line 3691 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 268:
#line 486 "slghparse.y" /* yacc.c:1646  */
    { string errmsg="Unknown export varnode: "+*(yyvsp[0].str); delete (yyvsp[0].str); yyerror(errmsg.c_str()); YYERROR; }
#line 3697 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 269:
#line 487 "slghparse.y" /* yacc.c:1646  */
    { string errmsg = "Subtable not attached to operand: "+(yyvsp[0].subtablesym)->getName(); yyerror(errmsg.c_str()); YYERROR; }
#line 3703 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 270:
#line 489 "slghparse.y" /* yacc.c:1646  */
    { (yyval.famsym) = (yyvsp[0].valuesym); }
#line 3709 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 271:
#line 490 "slghparse.y" /* yacc.c:1646  */
    { (yyval.famsym) = (yyvsp[0].valuemapsym); }
#line 3715 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 272:
#line 491 "slghparse.y" /* yacc.c:1646  */
    { (yyval.famsym) = (yyvsp[0].contextsym); }
#line 3721 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 273:
#line 492 "slghparse.y" /* yacc.c:1646  */
    { (yyval.famsym) = (yyvsp[0].namesym); }
#line 3727 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 274:
#line 493 "slghparse.y" /* yacc.c:1646  */
    { (yyval.famsym) = (yyvsp[0].varlistsym); }
#line 3733 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 275:
#line 495 "slghparse.y" /* yacc.c:1646  */
    { (yyval.specsym) = (yyvsp[0].varsym); }
#line 3739 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 276:
#line 496 "slghparse.y" /* yacc.c:1646  */
    { (yyval.specsym) = (yyvsp[0].specsym); }
#line 3745 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 277:
#line 497 "slghparse.y" /* yacc.c:1646  */
    { (yyval.specsym) = (yyvsp[0].operandsym); }
#line 3751 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 278:
#line 498 "slghparse.y" /* yacc.c:1646  */
    { (yyval.specsym) = (yyvsp[0].startsym); }
#line 3757 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 279:
#line 499 "slghparse.y" /* yacc.c:1646  */
    { (yyval.specsym) = (yyvsp[0].endsym); }
#line 3763 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 280:
#line 501 "slghparse.y" /* yacc.c:1646  */
    { (yyval.str) = new string; (*(yyval.str)) += (yyvsp[0].ch); }
#line 3769 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 281:
#line 502 "slghparse.y" /* yacc.c:1646  */
    { (yyval.str) = (yyvsp[-1].str); (*(yyval.str)) += (yyvsp[0].ch); }
#line 3775 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 282:
#line 504 "slghparse.y" /* yacc.c:1646  */
    { (yyval.biglist) = (yyvsp[-1].biglist); }
#line 3781 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 283:
#line 505 "slghparse.y" /* yacc.c:1646  */
    { (yyval.biglist) = new vector<intb>; (yyval.biglist)->push_back(intb(*(yyvsp[0].i))); delete (yyvsp[0].i); }
#line 3787 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 284:
#line 506 "slghparse.y" /* yacc.c:1646  */
    { (yyval.biglist) = new vector<intb>; (yyval.biglist)->push_back(-intb(*(yyvsp[0].i))); delete (yyvsp[0].i); }
#line 3793 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 285:
#line 508 "slghparse.y" /* yacc.c:1646  */
    { (yyval.biglist) = new vector<intb>; (yyval.biglist)->push_back(intb(*(yyvsp[0].i))); delete (yyvsp[0].i); }
#line 3799 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 286:
#line 509 "slghparse.y" /* yacc.c:1646  */
    { (yyval.biglist) = new vector<intb>; (yyval.biglist)->push_back(-intb(*(yyvsp[0].i))); delete (yyvsp[0].i); }
#line 3805 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 287:
#line 510 "slghparse.y" /* yacc.c:1646  */
    { if (*(yyvsp[0].str)!="_") { string errmsg = "Expecting integer but saw: "+*(yyvsp[0].str); delete (yyvsp[0].str); yyerror(errmsg.c_str()); YYERROR; }
                                  (yyval.biglist) = new vector<intb>; (yyval.biglist)->push_back((intb)0xBADBEEF); delete (yyvsp[0].str); }
#line 3812 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 288:
#line 512 "slghparse.y" /* yacc.c:1646  */
    { (yyval.biglist) = (yyvsp[-1].biglist); (yyval.biglist)->push_back(intb(*(yyvsp[0].i))); delete (yyvsp[0].i); }
#line 3818 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 289:
#line 513 "slghparse.y" /* yacc.c:1646  */
    { (yyval.biglist) = (yyvsp[-2].biglist); (yyval.biglist)->push_back(-intb(*(yyvsp[0].i))); delete (yyvsp[0].i); }
#line 3824 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 290:
#line 514 "slghparse.y" /* yacc.c:1646  */
    { if (*(yyvsp[0].str)!="_") { string errmsg = "Expecting integer but saw: "+*(yyvsp[0].str); delete (yyvsp[0].str); yyerror(errmsg.c_str()); YYERROR; }
                                  (yyval.biglist) = (yyvsp[-1].biglist); (yyval.biglist)->push_back((intb)0xBADBEEF); delete (yyvsp[0].str); }
#line 3831 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 291:
#line 517 "slghparse.y" /* yacc.c:1646  */
    { (yyval.strlist) = (yyvsp[-1].strlist); }
#line 3837 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 292:
#line 518 "slghparse.y" /* yacc.c:1646  */
    { (yyval.strlist) = new vector<string>; (yyval.strlist)->push_back(*(yyvsp[0].str)); delete (yyvsp[0].str); }
#line 3843 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 293:
#line 520 "slghparse.y" /* yacc.c:1646  */
    { (yyval.strlist) = new vector<string>; (yyval.strlist)->push_back( *(yyvsp[0].str) ); delete (yyvsp[0].str); }
#line 3849 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 294:
#line 521 "slghparse.y" /* yacc.c:1646  */
    { (yyval.strlist) = (yyvsp[-1].strlist); (yyval.strlist)->push_back(*(yyvsp[0].str)); delete (yyvsp[0].str); }
#line 3855 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 295:
#line 522 "slghparse.y" /* yacc.c:1646  */
    { string errmsg = (yyvsp[0].anysym)->getName()+": redefined"; yyerror(errmsg.c_str()); YYERROR; }
#line 3861 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 296:
#line 524 "slghparse.y" /* yacc.c:1646  */
    { (yyval.strlist) = (yyvsp[-1].strlist); }
#line 3867 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 297:
#line 526 "slghparse.y" /* yacc.c:1646  */
    { (yyval.strlist) = new vector<string>; (yyval.strlist)->push_back( *(yyvsp[0].str) ); delete (yyvsp[0].str); }
#line 3873 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 298:
#line 527 "slghparse.y" /* yacc.c:1646  */
    { (yyval.strlist) = new vector<string>; (yyval.strlist)->push_back( (yyvsp[0].anysym)->getName() ); }
#line 3879 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 299:
#line 528 "slghparse.y" /* yacc.c:1646  */
    { (yyval.strlist) = (yyvsp[-1].strlist); (yyval.strlist)->push_back(*(yyvsp[0].str)); delete (yyvsp[0].str); }
#line 3885 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 300:
#line 529 "slghparse.y" /* yacc.c:1646  */
    { (yyval.strlist) = (yyvsp[-1].strlist); (yyval.strlist)->push_back((yyvsp[0].anysym)->getName()); }
#line 3891 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 301:
#line 531 "slghparse.y" /* yacc.c:1646  */
    { (yyval.symlist) = (yyvsp[-1].symlist); }
#line 3897 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 302:
#line 532 "slghparse.y" /* yacc.c:1646  */
    { (yyval.symlist) = new vector<SleighSymbol *>; (yyval.symlist)->push_back((yyvsp[0].valuesym)); }
#line 3903 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 303:
#line 533 "slghparse.y" /* yacc.c:1646  */
    { (yyval.symlist) = new vector<SleighSymbol *>; (yyval.symlist)->push_back((yyvsp[0].contextsym)); }
#line 3909 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 304:
#line 535 "slghparse.y" /* yacc.c:1646  */
    { (yyval.symlist) = new vector<SleighSymbol *>; (yyval.symlist)->push_back( (yyvsp[0].valuesym) ); }
#line 3915 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 305:
#line 536 "slghparse.y" /* yacc.c:1646  */
    { (yyval.symlist) = new vector<SleighSymbol *>; (yyval.symlist)->push_back((yyvsp[0].contextsym)); }
#line 3921 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 306:
#line 537 "slghparse.y" /* yacc.c:1646  */
    { (yyval.symlist) = (yyvsp[-1].symlist); (yyval.symlist)->push_back((yyvsp[0].valuesym)); }
#line 3927 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 307:
#line 538 "slghparse.y" /* yacc.c:1646  */
    { (yyval.symlist) = (yyvsp[-1].symlist); (yyval.symlist)->push_back((yyvsp[0].contextsym)); }
#line 3933 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 308:
#line 539 "slghparse.y" /* yacc.c:1646  */
    { string errmsg = *(yyvsp[0].str)+": is not a value pattern"; delete (yyvsp[0].str); yyerror(errmsg.c_str()); YYERROR; }
#line 3939 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 309:
#line 541 "slghparse.y" /* yacc.c:1646  */
    { (yyval.symlist) = (yyvsp[-1].symlist); }
#line 3945 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 310:
#line 542 "slghparse.y" /* yacc.c:1646  */
    { (yyval.symlist) = new vector<SleighSymbol *>; (yyval.symlist)->push_back((yyvsp[0].varsym)); }
#line 3951 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 311:
#line 544 "slghparse.y" /* yacc.c:1646  */
    { (yyval.symlist) = new vector<SleighSymbol *>; (yyval.symlist)->push_back((yyvsp[0].varsym)); }
#line 3957 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 312:
#line 545 "slghparse.y" /* yacc.c:1646  */
    { if (*(yyvsp[0].str)!="_") { string errmsg = *(yyvsp[0].str)+": is not a varnode symbol"; delete (yyvsp[0].str); yyerror(errmsg.c_str()); YYERROR; }
				  (yyval.symlist) = new vector<SleighSymbol *>; (yyval.symlist)->push_back((SleighSymbol *)0); delete (yyvsp[0].str); }
#line 3964 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 313:
#line 547 "slghparse.y" /* yacc.c:1646  */
    { (yyval.symlist) = (yyvsp[-1].symlist); (yyval.symlist)->push_back((yyvsp[0].varsym)); }
#line 3970 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 314:
#line 548 "slghparse.y" /* yacc.c:1646  */
    { if (*(yyvsp[0].str)!="_") { string errmsg = *(yyvsp[0].str)+": is not a varnode symbol"; delete (yyvsp[0].str); yyerror(errmsg.c_str()); YYERROR; }
                                  (yyval.symlist) = (yyvsp[-1].symlist); (yyval.symlist)->push_back((SleighSymbol *)0); delete (yyvsp[0].str); }
#line 3977 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 315:
#line 551 "slghparse.y" /* yacc.c:1646  */
    { (yyval.param) = new vector<ExprTree *>; }
#line 3983 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 316:
#line 552 "slghparse.y" /* yacc.c:1646  */
    { (yyval.param) = new vector<ExprTree *>; (yyval.param)->push_back((yyvsp[0].tree)); }
#line 3989 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 317:
#line 553 "slghparse.y" /* yacc.c:1646  */
    { (yyval.param) = (yyvsp[-2].param); (yyval.param)->push_back((yyvsp[0].tree)); }
#line 3995 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 318:
#line 555 "slghparse.y" /* yacc.c:1646  */
    { (yyval.strlist) = new vector<string>; }
#line 4001 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 319:
#line 556 "slghparse.y" /* yacc.c:1646  */
    { (yyval.strlist) = new vector<string>; (yyval.strlist)->push_back(*(yyvsp[0].str)); delete (yyvsp[0].str); }
#line 4007 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 320:
#line 557 "slghparse.y" /* yacc.c:1646  */
    { (yyval.strlist) = (yyvsp[-2].strlist); (yyval.strlist)->push_back(*(yyvsp[0].str)); delete (yyvsp[0].str); }
#line 4013 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 321:
#line 559 "slghparse.y" /* yacc.c:1646  */
    { (yyval.anysym) = (yyvsp[0].spacesym); }
#line 4019 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 322:
#line 560 "slghparse.y" /* yacc.c:1646  */
    { (yyval.anysym) = (yyvsp[0].sectionsym); }
#line 4025 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 323:
#line 561 "slghparse.y" /* yacc.c:1646  */
    { (yyval.anysym) = (yyvsp[0].tokensym); }
#line 4031 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 324:
#line 562 "slghparse.y" /* yacc.c:1646  */
    { (yyval.anysym) = (yyvsp[0].useropsym); }
#line 4037 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 325:
#line 563 "slghparse.y" /* yacc.c:1646  */
    { (yyval.anysym) = (yyvsp[0].macrosym); }
#line 4043 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 326:
#line 564 "slghparse.y" /* yacc.c:1646  */
    { (yyval.anysym) = (yyvsp[0].subtablesym); }
#line 4049 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 327:
#line 565 "slghparse.y" /* yacc.c:1646  */
    { (yyval.anysym) = (yyvsp[0].valuesym); }
#line 4055 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 328:
#line 566 "slghparse.y" /* yacc.c:1646  */
    { (yyval.anysym) = (yyvsp[0].valuemapsym); }
#line 4061 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 329:
#line 567 "slghparse.y" /* yacc.c:1646  */
    { (yyval.anysym) = (yyvsp[0].contextsym); }
#line 4067 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 330:
#line 568 "slghparse.y" /* yacc.c:1646  */
    { (yyval.anysym) = (yyvsp[0].namesym); }
#line 4073 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 331:
#line 569 "slghparse.y" /* yacc.c:1646  */
    { (yyval.anysym) = (yyvsp[0].varsym); }
#line 4079 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 332:
#line 570 "slghparse.y" /* yacc.c:1646  */
    { (yyval.anysym) = (yyvsp[0].varlistsym); }
#line 4085 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 333:
#line 571 "slghparse.y" /* yacc.c:1646  */
    { (yyval.anysym) = (yyvsp[0].operandsym); }
#line 4091 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 334:
#line 572 "slghparse.y" /* yacc.c:1646  */
    { (yyval.anysym) = (yyvsp[0].startsym); }
#line 4097 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 335:
#line 573 "slghparse.y" /* yacc.c:1646  */
    { (yyval.anysym) = (yyvsp[0].endsym); }
#line 4103 "slghparse.cc" /* yacc.c:1646  */
    break;

  case 336:
#line 574 "slghparse.y" /* yacc.c:1646  */
    { (yyval.anysym) = (yyvsp[0].bitsym); }
#line 4109 "slghparse.cc" /* yacc.c:1646  */
    break;


#line 4113 "slghparse.cc" /* yacc.c:1646  */
      default: break;
    }
  /* User semantic actions sometimes alter yychar, and that requires
     that yytoken be updated with the new translation.  We take the
     approach of translating immediately before every use of yytoken.
     One alternative is translating here after every semantic action,
     but that translation would be missed if the semantic action invokes
     YYABORT, YYACCEPT, or YYERROR immediately after altering yychar or
     if it invokes YYBACKUP.  In the case of YYABORT or YYACCEPT, an
     incorrect destructor might then be invoked immediately.  In the
     case of YYERROR or YYBACKUP, subsequent parser actions might lead
     to an incorrect destructor call or verbose syntax error message
     before the lookahead is translated.  */
  YY_SYMBOL_PRINT ("-> $$ =", yyr1[yyn], &yyval, &yyloc);

  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);

  *++yyvsp = yyval;

  /* Now 'shift' the result of the reduction.  Determine what state
     that goes to, based on the state we popped back to and the rule
     number reduced by.  */

  yyn = yyr1[yyn];

  yystate = yypgoto[yyn - YYNTOKENS] + *yyssp;
  if (0 <= yystate && yystate <= YYLAST && yycheck[yystate] == *yyssp)
    yystate = yytable[yystate];
  else
    yystate = yydefgoto[yyn - YYNTOKENS];

  goto yynewstate;


/*--------------------------------------.
| yyerrlab -- here on detecting error.  |
`--------------------------------------*/
yyerrlab:
  /* Make sure we have latest lookahead translation.  See comments at
     user semantic actions for why this is necessary.  */
  yytoken = yychar == YYEMPTY ? YYEMPTY : YYTRANSLATE (yychar);

  /* If not already recovering from an error, report this error.  */
  if (!yyerrstatus)
    {
      ++yynerrs;
#if ! YYERROR_VERBOSE
      yyerror (YY_("syntax error"));
#else
# define YYSYNTAX_ERROR yysyntax_error (&yymsg_alloc, &yymsg, \
                                        yyssp, yytoken)
      {
        char const *yymsgp = YY_("syntax error");
        int yysyntax_error_status;
        yysyntax_error_status = YYSYNTAX_ERROR;
        if (yysyntax_error_status == 0)
          yymsgp = yymsg;
        else if (yysyntax_error_status == 1)
          {
            if (yymsg != yymsgbuf)
              YYSTACK_FREE (yymsg);
            yymsg = (char *) YYSTACK_ALLOC (yymsg_alloc);
            if (!yymsg)
              {
                yymsg = yymsgbuf;
                yymsg_alloc = sizeof yymsgbuf;
                yysyntax_error_status = 2;
              }
            else
              {
                yysyntax_error_status = YYSYNTAX_ERROR;
                yymsgp = yymsg;
              }
          }
        yyerror (yymsgp);
        if (yysyntax_error_status == 2)
          goto yyexhaustedlab;
      }
# undef YYSYNTAX_ERROR
#endif
    }



  if (yyerrstatus == 3)
    {
      /* If just tried and failed to reuse lookahead token after an
         error, discard it.  */

      if (yychar <= YYEOF)
        {
          /* Return failure if at end of input.  */
          if (yychar == YYEOF)
            YYABORT;
        }
      else
        {
          yydestruct ("Error: discarding",
                      yytoken, &yylval);
          yychar = YYEMPTY;
        }
    }

  /* Else will try to reuse lookahead token after shifting the error
     token.  */
  goto yyerrlab1;


/*---------------------------------------------------.
| yyerrorlab -- error raised explicitly by YYERROR.  |
`---------------------------------------------------*/
yyerrorlab:

  /* Pacify compilers like GCC when the user code never invokes
     YYERROR and the label yyerrorlab therefore never appears in user
     code.  */
  if (/*CONSTCOND*/ 0)
     goto yyerrorlab;

  /* Do not reclaim the symbols of the rule whose action triggered
     this YYERROR.  */
  YYPOPSTACK (yylen);
  yylen = 0;
  YY_STACK_PRINT (yyss, yyssp);
  yystate = *yyssp;
  goto yyerrlab1;


/*-------------------------------------------------------------.
| yyerrlab1 -- common code for both syntax error and YYERROR.  |
`-------------------------------------------------------------*/
yyerrlab1:
  yyerrstatus = 3;      /* Each real token shifted decrements this.  */

  for (;;)
    {
      yyn = yypact[yystate];
      if (!yypact_value_is_default (yyn))
        {
          yyn += YYTERROR;
          if (0 <= yyn && yyn <= YYLAST && yycheck[yyn] == YYTERROR)
            {
              yyn = yytable[yyn];
              if (0 < yyn)
                break;
            }
        }

      /* Pop the current state because it cannot handle the error token.  */
      if (yyssp == yyss)
        YYABORT;


      yydestruct ("Error: popping",
                  yystos[yystate], yyvsp);
      YYPOPSTACK (1);
      yystate = *yyssp;
      YY_STACK_PRINT (yyss, yyssp);
    }

  YY_IGNORE_MAYBE_UNINITIALIZED_BEGIN
  *++yyvsp = yylval;
  YY_IGNORE_MAYBE_UNINITIALIZED_END


  /* Shift the error token.  */
  YY_SYMBOL_PRINT ("Shifting", yystos[yyn], yyvsp, yylsp);

  yystate = yyn;
  goto yynewstate;


/*-------------------------------------.
| yyacceptlab -- YYACCEPT comes here.  |
`-------------------------------------*/
yyacceptlab:
  yyresult = 0;
  goto yyreturn;

/*-----------------------------------.
| yyabortlab -- YYABORT comes here.  |
`-----------------------------------*/
yyabortlab:
  yyresult = 1;
  goto yyreturn;

#if !defined yyoverflow || YYERROR_VERBOSE
/*-------------------------------------------------.
| yyexhaustedlab -- memory exhaustion comes here.  |
`-------------------------------------------------*/
yyexhaustedlab:
  yyerror (YY_("memory exhausted"));
  yyresult = 2;
  /* Fall through.  */
#endif

yyreturn:
  if (yychar != YYEMPTY)
    {
      /* Make sure we have latest lookahead translation.  See comments at
         user semantic actions for why this is necessary.  */
      yytoken = YYTRANSLATE (yychar);
      yydestruct ("Cleanup: discarding lookahead",
                  yytoken, &yylval);
    }
  /* Do not reclaim the symbols of the rule whose action triggered
     this YYABORT or YYACCEPT.  */
  YYPOPSTACK (yylen);
  YY_STACK_PRINT (yyss, yyssp);
  while (yyssp != yyss)
    {
      yydestruct ("Cleanup: popping",
                  yystos[*yyssp], yyvsp);
      YYPOPSTACK (1);
    }
#ifndef yyoverflow
  if (yyss != yyssa)
    YYSTACK_FREE (yyss);
#endif
#if YYERROR_VERBOSE
  if (yymsg != yymsgbuf)
    YYSTACK_FREE (yymsg);
#endif
  return yyresult;
}
#line 576 "slghparse.y" /* yacc.c:1906  */


int yyerror(const char *s)

{
  slgh->reportError(s);
  return 0;
}
