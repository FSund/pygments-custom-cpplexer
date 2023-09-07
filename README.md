# pygments-custom

A custom lexer for [Pygments](http://pygments.org/) for extra keyword
highlighting when using the [minted](https://github.com/gpoore/minted)
package in LaTeX. This was inspired by [FSund's Molecular
Dynamics](https://github.com/FSund/pygments-custom-cpplexer.git) extension.

## Example output

[examples/example.pdf](examples/example.pdf)

## Capabilities

You can define any identifier (e.g., `vec3`) to be any of the subtypes
of `Keyword` that pygments recognizes (or, in fact, any token at all).
As of 2023, pygments uses:

* `Keyword.Type`  ← This is probably what you want.
* `Keyword.Constant`
* `Keyword.Declaration`
* `Keyword.Namespace`
* `Keyword.Pseudo`
* `Keyword.Removed`
* `Keyword.Reserved`
* `Keyword` (a generic Keyword token)

By default, the CustomLexer inherits Keywords from the C Lexer, but
that is easily changed.

## Customization

Edit the file [pygments_custom/__init.py__](pygments_custom/__init.py__)
and simply list the keywords in the array you'd like. For example:

``` python
EXTRA[Keyword.Type] = ['FLAG', 'vec3', 'Atom' ]
EXTRA[Keyword.Constant] = [ 'M_PI', 'Tau' ]
```

### Changing the super class for lexing

The default super class is "C" as seen in the first line of `__init.py__`:

``` python
from pygments.lexers.compiled import CLexer as mysuper
```

To inherit from the C++ lexer, for example, one would change it to say:
``` python
from pygments.lexers.compiled import CppLexer as mysuper
```

## Install

    git clone https://github.com/hackerb9/pygments-custom
    cd pygments-custom
    (sudo) python setup.py install

### Verify

Verify that the package installed correctly by checking if "custom" is
in the list of lexers. You can run:

    pygmentize -L lexers | grep custom

## Using the lexer in latex

Just use the **custom** "language". In LaTeX this means something like this

``` latex
\begin{minted}{custom}
vec3 position(0.0, 0.0, 0.0);
Atom *atom = new Atom(position);
\end{minted}

```

You can test it using the [example.ltx](example.ltx) file like so:

    pdflatex -shell-escape example.ltx

See the minted package at https://github.com/gpoore/minted for more information.

## Problems

* If after changing the `__init__.py` and reinstalling the module, it
  doesn't seem to have an effect in latex, try removing the
  `_minted-filename` directory which caches the pygments lexer.

  If you will be editing the lexer often, you may wish to disable the
  cache completely like so:
  
  ```latex
  \usepackage[cache=false]{minted}
  ```
  
* If you get strange errors halting latex from running, delete
  minted's *.out.pyg file. 

* Different Keyword subtypes may not look different depending on the
  inherited lexer and the style chosen. When subclassing from CLexer
  and using the default style, Constant, Declaration, Namespace,
  Pseudo, and Reserved all look the same as a generic Keyword. 
  
## Different styles

To emphasize certain subtypes, one can use a different style
(`\setminted{style=tango}`). For example, the "algol" style makes
namespaces distinct from other keywords by italicizing them.

Some of the styles presume a dark background but rely on the user to
set it, like so: `\setminted{style=github-dark, bgcolor=darkgray}`

### Available styles (2023)

`python -c "import pygments.styles; print(list(pygments.styles.get_all_styles()))"`

['default', 'emacs', 'friendly', 'friendly_grayscale', 'colorful', 'autumn', 'murphy', 'manni', 'material', 'monokai', 'perldoc', 'pastie', 'borland', 'trac', 'native', 'fruity', 'bw', 'vim', 'vs', 'tango', 'rrt', 'xcode', 'igor', 'paraiso-light', 'paraiso-dark', 'lovelace', 'algol', 'algol_nu', 'arduino', 'rainbow_dash', 'abap', 'solarized-dark', 'solarized-light', 'sas', 'staroffice', 'stata', 'stata-light', 'stata-dark', 'inkpot', 'zenburn', 'gruvbox-dark', 'gruvbox-light', 'dracula', 'one-dark', 'lilypond', 'nord', 'nord-darker', 'github-dark']


## Possible lexers to inherit from (as of 2023)

`python -c "import pygments.lexers; print(pygments.lexers.__all__)"`

['get_lexer_by_name', 'get_lexer_for_filename', 'find_lexer_class', 'guess_lexer', 'load_lexer_from_file', 'ABAPLexer', 'AMDGPULexer', 'APLLexer', 'AbnfLexer', 'ActionScript3Lexer', 'ActionScriptLexer', 'AdaLexer', 'AdlLexer', 'AgdaLexer', 'AheuiLexer', 'AlloyLexer', 'AmbientTalkLexer', 'AmplLexer', 'Angular2HtmlLexer', 'Angular2Lexer', 'AntlrActionScriptLexer', 'AntlrCSharpLexer', 'AntlrCppLexer', 'AntlrJavaLexer', 'AntlrLexer', 'AntlrObjectiveCLexer', 'AntlrPerlLexer', 'AntlrPythonLexer', 'AntlrRubyLexer', 'ApacheConfLexer', 'AppleScriptLexer', 'ArduinoLexer', 'ArrowLexer', 'ArturoLexer', 'AscLexer', 'AspectJLexer', 'AsymptoteLexer', 'AugeasLexer', 'AutoItLexer', 'AutohotkeyLexer', 'AwkLexer', 'BBCBasicLexer', 'BBCodeLexer', 'BCLexer', 'BSTLexer', 'BareLexer', 'BaseMakefileLexer', 'BashLexer', 'BashSessionLexer', 'BatchLexer', 'BddLexer', 'BefungeLexer', 'BerryLexer', 'BibTeXLexer', 'BlitzBasicLexer', 'BlitzMaxLexer', 'BnfLexer', 'BoaLexer', 'BooLexer', 'BoogieLexer', 'BrainfuckLexer', 'BugsLexer', 'CAmkESLexer', 'CLexer', 'CMakeLexer', 'CObjdumpLexer', 'CPSALexer', 'CSSUL4Lexer', 'CSharpAspxLexer', 'CSharpLexer', 'Ca65Lexer', 'CadlLexer', 'CapDLLexer', 'CapnProtoLexer', 'CarbonLexer', 'CbmBasicV2Lexer', 'CddlLexer', 'CeylonLexer', 'Cfengine3Lexer', 'ChaiscriptLexer', 'ChapelLexer', 'CharmciLexer', 'CheetahHtmlLexer', 'CheetahJavascriptLexer', 'CheetahLexer', 'CheetahXmlLexer', 'CirruLexer', 'ClayLexer', 'CleanLexer', 'ClojureLexer', 'ClojureScriptLexer', 'CobolFreeformatLexer', 'CobolLexer', 'CoffeeScriptLexer', 'ColdfusionCFCLexer', 'ColdfusionHtmlLexer', 'ColdfusionLexer', 'Comal80Lexer', 'CommonLispLexer', 'ComponentPascalLexer', 'CoqLexer', 'CplintLexer', 'CppLexer', 'CppObjdumpLexer', 'CrmshLexer', 'CrocLexer', 'CryptolLexer', 'CrystalLexer', 'CsoundDocumentLexer', 'CsoundOrchestraLexer', 'CsoundScoreLexer', 'CssDjangoLexer', 'CssErbLexer', 'CssGenshiLexer', 'CssLexer', 'CssPhpLexer', 'CssSmartyLexer', 'CudaLexer', 'CypherLexer', 'CythonLexer', 'DLexer', 'DObjdumpLexer', 'DarcsPatchLexer', 'DartLexer', 'Dasm16Lexer', 'DaxLexer', 'DebianControlLexer', 'DelphiLexer', 'DevicetreeLexer', 'DgLexer', 'DiffLexer', 'DjangoLexer', 'DockerLexer', 'DtdLexer', 'DuelLexer', 'DylanConsoleLexer', 'DylanLexer', 'DylanLidLexer', 'ECLLexer', 'ECLexer', 'EarlGreyLexer', 'EasytrieveLexer', 'EbnfLexer', 'EiffelLexer', 'ElixirConsoleLexer', 'ElixirLexer', 'ElmLexer', 'ElpiLexer', 'EmacsLispLexer', 'EmailLexer', 'ErbLexer', 'ErlangLexer', 'ErlangShellLexer', 'EvoqueHtmlLexer', 'EvoqueLexer', 'EvoqueXmlLexer', 'ExeclineLexer', 'EzhilLexer', 'FSharpLexer', 'FStarLexer', 'FactorLexer', 'FancyLexer', 'FantomLexer', 'FelixLexer', 'FennelLexer', 'FiftLexer', 'FishShellLexer', 'FlatlineLexer', 'FloScriptLexer', 'ForthLexer', 'FortranFixedLexer', 'FortranLexer', 'FoxProLexer', 'FreeFemLexer', 'FuncLexer', 'FutharkLexer', 'GAPConsoleLexer', 'GAPLexer', 'GDScriptLexer', 'GLShaderLexer', 'GSQLLexer', 'GasLexer', 'GcodeLexer', 'GenshiLexer', 'GenshiTextLexer', 'GettextLexer', 'GherkinLexer', 'GnuplotLexer', 'GoLexer', 'GoloLexer', 'GoodDataCLLexer', 'GosuLexer', 'GosuTemplateLexer', 'GraphvizLexer', 'GroffLexer', 'GroovyLexer', 'HLSLShaderLexer', 'HTMLUL4Lexer', 'HamlLexer', 'HandlebarsHtmlLexer', 'HandlebarsLexer', 'HaskellLexer', 'HaxeLexer', 'HexdumpLexer', 'HsailLexer', 'HspecLexer', 'HtmlDjangoLexer', 'HtmlGenshiLexer', 'HtmlLexer', 'HtmlPhpLexer', 'HtmlSmartyLexer', 'HttpLexer', 'HxmlLexer', 'HyLexer', 'HybrisLexer', 'IDLLexer', 'IconLexer', 'IdrisLexer', 'IgorLexer', 'Inform6Lexer', 'Inform6TemplateLexer', 'Inform7Lexer', 'IniLexer', 'IoLexer', 'IokeLexer', 'IrcLogsLexer', 'IsabelleLexer', 'JLexer', 'JMESPathLexer', 'JSLTLexer', 'JagsLexer', 'JasminLexer', 'JavaLexer', 'JavascriptDjangoLexer', 'JavascriptErbLexer', 'JavascriptGenshiLexer', 'JavascriptLexer', 'JavascriptPhpLexer', 'JavascriptSmartyLexer', 'JavascriptUL4Lexer', 'JclLexer', 'JsgfLexer', 'JsonBareObjectLexer', 'JsonLdLexer', 'JsonLexer', 'JsonnetLexer', 'JspLexer', 'JuliaConsoleLexer', 'JuliaLexer', 'JuttleLexer', 'KLexer', 'KalLexer', 'KconfigLexer', 'KernelLogLexer', 'KokaLexer', 'KotlinLexer', 'KuinLexer', 'LSLLexer', 'LassoCssLexer', 'LassoHtmlLexer', 'LassoJavascriptLexer', 'LassoLexer', 'LassoXmlLexer', 'LeanLexer', 'LessCssLexer', 'LighttpdConfLexer', 'LilyPondLexer', 'LimboLexer', 'LiquidLexer', 'LiterateAgdaLexer', 'LiterateCryptolLexer', 'LiterateHaskellLexer', 'LiterateIdrisLexer', 'LiveScriptLexer', 'LlvmLexer', 'LlvmMirBodyLexer', 'LlvmMirLexer', 'LogosLexer', 'LogtalkLexer', 'LuaLexer', 'MCFunctionLexer', 'MCSchemaLexer', 'MIMELexer', 'MIPSLexer', 'MOOCodeLexer', 'MSDOSSessionLexer', 'Macaulay2Lexer', 'MakefileLexer', 'MakoCssLexer', 'MakoHtmlLexer', 'MakoJavascriptLexer', 'MakoLexer', 'MakoXmlLexer', 'MaqlLexer', 'MarkdownLexer', 'MaskLexer', 'MasonLexer', 'MathematicaLexer', 'MatlabLexer', 'MatlabSessionLexer', 'MaximaLexer', 'MesonLexer', 'MiniDLexer', 'MiniScriptLexer', 'ModelicaLexer', 'Modula2Lexer', 'MoinWikiLexer', 'MonkeyLexer', 'MonteLexer', 'MoonScriptLexer', 'MoselLexer', 'MozPreprocCssLexer', 'MozPreprocHashLexer', 'MozPreprocJavascriptLexer', 'MozPreprocPercentLexer', 'MozPreprocXulLexer', 'MqlLexer', 'MscgenLexer', 'MuPADLexer', 'MxmlLexer', 'MySqlLexer', 'MyghtyCssLexer', 'MyghtyHtmlLexer', 'MyghtyJavascriptLexer', 'MyghtyLexer', 'MyghtyXmlLexer', 'NCLLexer', 'NSISLexer', 'NasmLexer', 'NasmObjdumpLexer', 'NemerleLexer', 'NesCLexer', 'NestedTextLexer', 'NewLispLexer', 'NewspeakLexer', 'NginxConfLexer', 'NimrodLexer', 'NitLexer', 'NixLexer', 'NodeConsoleLexer', 'NotmuchLexer', 'NuSMVLexer', 'NumPyLexer', 'ObjdumpLexer', 'ObjectiveCLexer', 'ObjectiveCppLexer', 'ObjectiveJLexer', 'OcamlLexer', 'OctaveLexer', 'OdinLexer', 'OmgIdlLexer', 'OocLexer', 'OpaLexer', 'OpenEdgeLexer', 'OutputLexer', 'PacmanConfLexer', 'PanLexer', 'ParaSailLexer', 'PawnLexer', 'PegLexer', 'Perl6Lexer', 'PerlLexer', 'PhixLexer', 'PhpLexer', 'PigLexer', 'PikeLexer', 'PkgConfigLexer', 'PlPgsqlLexer', 'PointlessLexer', 'PonyLexer', 'PortugolLexer', 'PostScriptLexer', 'PostgresConsoleLexer', 'PostgresExplainLexer', 'PostgresLexer', 'PovrayLexer', 'PowerShellLexer', 'PowerShellSessionLexer', 'PraatLexer', 'ProcfileLexer', 'PrologLexer', 'PromQLLexer', 'PropertiesLexer', 'ProtoBufLexer', 'PsyshConsoleLexer', 'PugLexer', 'PuppetLexer', 'PyPyLogLexer', 'Python2Lexer', 'Python2TracebackLexer', 'PythonConsoleLexer', 'PythonLexer', 'PythonTracebackLexer', 'PythonUL4Lexer', 'QBasicLexer', 'QLexer', 'QVToLexer', 'QlikLexer', 'QmlLexer', 'RConsoleLexer', 'RNCCompactLexer', 'RPMSpecLexer', 'RacketLexer', 'RagelCLexer', 'RagelCppLexer', 'RagelDLexer', 'RagelEmbeddedLexer', 'RagelJavaLexer', 'RagelLexer', 'RagelObjectiveCLexer', 'RagelRubyLexer', 'RawTokenLexer', 'RdLexer', 'ReasonLexer', 'RebolLexer', 'RedLexer', 'RedcodeLexer', 'RegeditLexer', 'ResourceLexer', 'RexxLexer', 'RhtmlLexer', 'RideLexer', 'RitaLexer', 'RoboconfGraphLexer', 'RoboconfInstancesLexer', 'RobotFrameworkLexer', 'RqlLexer', 'RslLexer', 'RstLexer', 'RtsLexer', 'RubyConsoleLexer', 'RubyLexer', 'RustLexer', 'SASLexer', 'SLexer', 'SMLLexer', 'SNBTLexer', 'SarlLexer', 'SassLexer', 'SaviLexer', 'ScalaLexer', 'ScamlLexer', 'ScdocLexer', 'SchemeLexer', 'ScilabLexer', 'ScssLexer', 'SedLexer', 'ShExCLexer', 'ShenLexer', 'SieveLexer', 'SilverLexer', 'SingularityLexer', 'SlashLexer', 'SlimLexer', 'SlurmBashLexer', 'SmaliLexer', 'SmalltalkLexer', 'SmartGameFormatLexer', 'SmartyLexer', 'SmithyLexer', 'SnobolLexer', 'SnowballLexer', 'SolidityLexer', 'SophiaLexer', 'SourcePawnLexer', 'SourcesListLexer', 'SparqlLexer', 'SpiceLexer', 'SqlJinjaLexer', 'SqlLexer', 'SqliteConsoleLexer', 'SquidConfLexer', 'SrcinfoLexer', 'SspLexer', 'StanLexer', 'StataLexer', 'SuperColliderLexer', 'SwiftLexer', 'SwigLexer', 'SystemVerilogLexer', 'TAPLexer', 'TNTLexer', 'TOMLLexer', 'Tads3Lexer', 'TalLexer', 'TasmLexer', 'TclLexer', 'TcshLexer', 'TcshSessionLexer', 'TeaTemplateLexer', 'TealLexer', 'TeraTermLexer', 'TermcapLexer', 'TerminfoLexer', 'TerraformLexer', 'TexLexer', 'TextLexer', 'ThingsDBLexer', 'ThriftLexer', 'TiddlyWiki5Lexer', 'TlbLexer', 'TodotxtLexer', 'TransactSqlLexer', 'TreetopLexer', 'TurtleLexer', 'TwigHtmlLexer', 'TwigLexer', 'TypeScriptLexer', 'TypoScriptCssDataLexer', 'TypoScriptHtmlDataLexer', 'TypoScriptLexer', 'UL4Lexer', 'UcodeLexer', 'UniconLexer', 'UnixConfigLexer', 'UrbiscriptLexer', 'UsdLexer', 'VBScriptLexer', 'VCLLexer', 'VCLSnippetLexer', 'VCTreeStatusLexer', 'VGLLexer', 'ValaLexer', 'VbNetAspxLexer', 'VbNetLexer', 'VelocityHtmlLexer', 'VelocityLexer', 'VelocityXmlLexer', 'VerilogLexer', 'VhdlLexer', 'VimLexer', 'WDiffLexer', 'WatLexer', 'WebIDLLexer', 'WgslLexer', 'WhileyLexer', 'WikitextLexer', 'WoWTocLexer', 'WrenLexer', 'X10Lexer', 'XMLUL4Lexer', 'XQueryLexer', 'XmlDjangoLexer', 'XmlErbLexer', 'XmlLexer', 'XmlPhpLexer', 'XmlSmartyLexer', 'XorgLexer', 'XppLexer', 'XsltLexer', 'XtendLexer', 'XtlangLexer', 'YamlJinjaLexer', 'YamlLexer', 'YangLexer', 'ZeekLexer', 'ZephirLexer', 'ZigLexer', 'apdlexer', 'Python3Lexer', 'Python3TracebackLexer']
