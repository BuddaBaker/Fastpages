---
keywords: fastai
title: Title
nb_path: _notebooks/2022-09-22-Javascript.ipynb
layout: notebook
---

<!--
#################################################
### THIS FILE WAS AUTOGENERATED! DO NOT EDIT! ###
#################################################
# file to edit: _notebooks/2022-09-22-Javascript.ipynb
-->

<div class="container" id="notebook-container">
        
    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">function</span> <span class="n">logItType</span><span class="p">(</span><span class="n">output</span><span class="p">)</span> <span class="p">{</span>
    <span class="n">console</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="n">typeof</span> <span class="n">output</span><span class="p">,</span> <span class="s2">&quot;;&quot;</span><span class="p">,</span> <span class="n">output</span><span class="p">);</span>
<span class="p">}</span>
<span class="n">console</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="s2">&quot;Looking at dynamic nature of types in JavaScript&quot;</span><span class="p">)</span>
<span class="n">logItType</span><span class="p">(</span><span class="s2">&quot;hello&quot;</span><span class="p">);</span> <span class="o">//</span> <span class="n">String</span>
<span class="n">logItType</span><span class="p">(</span><span class="mi">2020</span><span class="p">);</span>    <span class="o">//</span> <span class="n">Number</span>
<span class="n">logItType</span><span class="p">([</span><span class="mi">1</span><span class="p">,</span> <span class="mi">2</span><span class="p">,</span> <span class="mi">3</span><span class="p">]);</span>  <span class="o">//</span> <span class="n">Obje</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-intense-fg ansi-bold">Failed to start the Kernel. 
</span>
<span class="ansi-red-intense-fg ansi-bold">module.js:597
</span>
<span class="ansi-red-intense-fg ansi-bold">  return process.dlopen(module, path._makeLong(filename));
</span>
<span class="ansi-red-intense-fg ansi-bold">                 ^
</span>
<span class="ansi-red-intense-fg ansi-bold">
</span>
<span class="ansi-red-intense-fg ansi-bold">Error: /home/prasithchilla/anaconda3/bin/../lib/libstdc++.so.6: version `GLIBCXX_3.4.29&#39; not found (required by /home/prasithchilla/anaconda3/lib/node_modules/ijavascript/node_modules/zeromq/build/Release/zmq.node)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at Error (native)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at Object.Module._extensions..node (module.js:597:18)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at Module.load (module.js:487:32)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at tryModuleLoad (module.js:446:12)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at Function.Module._load (module.js:438:3)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at Module.require (module.js:497:17)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at require (internal/module.js:20:19)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at load (/home/prasithchilla/anaconda3/lib/node_modules/ijavascript/node_modules/node-gyp-build/index.js:22:10)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at Object.&lt;anonymous&gt; (/home/prasithchilla/anaconda3/lib/node_modules/ijavascript/node_modules/zeromq/binding.js:1:105)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at Module._compile (module.js:570:32). 
</span>
<span class="ansi-red-intense-fg ansi-bold">View Jupyter &lt;a href=&#39;command:jupyter.viewOutput&#39;&gt;log&lt;/a&gt; for further details.</span></pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

    {% raw %}
    
<div class="cell border-box-sizing code_cell rendered">
<div class="input">

<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">console</span><span class="o">.</span><span class="n">log</span><span class="p">(</span><span class="s2">&quot;hi&quot;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">

<div class="output_area">

<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-red-intense-fg ansi-bold">Failed to start the Kernel. 
</span>
<span class="ansi-red-intense-fg ansi-bold">module.js:597
</span>
<span class="ansi-red-intense-fg ansi-bold">  return process.dlopen(module, path._makeLong(filename));
</span>
<span class="ansi-red-intense-fg ansi-bold">                 ^
</span>
<span class="ansi-red-intense-fg ansi-bold">
</span>
<span class="ansi-red-intense-fg ansi-bold">Error: /home/prasithchilla/anaconda3/bin/../lib/libstdc++.so.6: version `GLIBCXX_3.4.29&#39; not found (required by /home/prasithchilla/anaconda3/lib/node_modules/ijavascript/node_modules/zeromq/build/Release/zmq.node)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at Error (native)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at Object.Module._extensions..node (module.js:597:18)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at Module.load (module.js:487:32)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at tryModuleLoad (module.js:446:12)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at Function.Module._load (module.js:438:3)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at Module.require (module.js:497:17)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at require (internal/module.js:20:19)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at load (/home/prasithchilla/anaconda3/lib/node_modules/ijavascript/node_modules/node-gyp-build/index.js:22:10)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at Object.&lt;anonymous&gt; (/home/prasithchilla/anaconda3/lib/node_modules/ijavascript/node_modules/zeromq/binding.js:1:105)
</span>
<span class="ansi-red-intense-fg ansi-bold">    at Module._compile (module.js:570:32). 
</span>
<span class="ansi-red-intense-fg ansi-bold">View Jupyter &lt;a href=&#39;command:jupyter.viewOutput&#39;&gt;log&lt;/a&gt; for further details.</span></pre>
</div>
</div>

</div>
</div>

</div>
    {% endraw %}

</div>
 

