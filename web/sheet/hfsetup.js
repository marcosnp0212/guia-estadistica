(function(H){
var T=H.FunctionArgumentType,CE=H.CellError,ET=H.ErrorType;
function nums(self,r){var v=self.arithmeticHelper.manyToExactNumbers(r.valuesFromTopLeftCorner());return v;}
function pctInc(v,k){v=v.slice().sort(function(a,b){return a-b;});var p=(v.length-1)*k,lo=Math.floor(p),hi=Math.ceil(p);return v[lo]+(v[hi]-v[lo])*(p-lo);}
function pairs(self,ry,rx){var y=ry.valuesFromTopLeftCorner(),x=rx.valuesFromTopLeftCorner();if(x.length!==y.length)return new CE(ET.NA);
  var X=[],Y=[];for(var i=0;i<x.length;i++)if(typeof x[i]==='number'&&typeof y[i]==='number'){X.push(x[i]);Y.push(y[i]);}
  if(X.length<2)return new CE(ET.DIV_BY_ZERO);var mx=0,my=0;X.forEach(function(a){mx+=a;});Y.forEach(function(a){my+=a;});mx/=X.length;my/=Y.length;
  var sxy=0,sxx=0;for(var j=0;j<X.length;j++){sxy+=(X[j]-mx)*(Y[j]-my);sxx+=(X[j]-mx)*(X[j]-mx);}if(sxx===0)return new CE(ET.DIV_BY_ZERO);var b=sxy/sxx;return{b:b,a:my-b*mx};}
class P extends H.FunctionPlugin{
  mode(ast,st){return this.runFunction(ast.args,st,this.metadata('MODE.SNGL'),function(){var v=[];for(var i=0;i<arguments.length;i++){var a=arguments[i];if(a&&a.valuesFromTopLeftCorner)v=v.concat(nums(this,a));else if(typeof a==='number')v.push(a);}
    var c=new Map(),best=null,bc=1;v.forEach(function(x){var n=(c.get(x)||0)+1;c.set(x,n);});v.forEach(function(x){if(c.get(x)>bc){bc=c.get(x);best=x;}});return best===null?new CE(ET.NA):best;}.bind(this));}
  quart(ast,st){return this.runFunction(ast.args,st,this.metadata('QUARTILE.INC'),function(r,q){var v=nums(this,r);q=Math.trunc(q);if(!v.length||q<0||q>4)return new CE(ET.NUM);return pctInc(v,q/4);}.bind(this));}
  perc(ast,st){return this.runFunction(ast.args,st,this.metadata('PERCENTILE.INC'),function(r,k){var v=nums(this,r);if(!v.length||k<0||k>1)return new CE(ET.NUM);return pctInc(v,k);}.bind(this));}
  fore(ast,st){return this.runFunction(ast.args,st,this.metadata('FORECAST.LINEAR'),function(x,ry,rx){var p=pairs(this,ry,rx);if(p instanceof CE)return p;return p.a+p.b*x;}.bind(this));}
  inter(ast,st){return this.runFunction(ast.args,st,this.metadata('INTERCEPT'),function(ry,rx){var p=pairs(this,ry,rx);if(p instanceof CE)return p;return p.a;}.bind(this));}
  kurt(ast,st){return this.runFunction(ast.args,st,this.metadata('KURT'),function(){var v=[];for(var i=0;i<arguments.length;i++){var a=arguments[i];if(a&&a.valuesFromTopLeftCorner)v=v.concat(nums(this,a));else if(typeof a==='number')v.push(a);}
    var n=v.length;if(n<4)return new CE(ET.DIV_BY_ZERO);var m=v.reduce(function(s,x){return s+x;},0)/n,s2=v.reduce(function(s,x){return s+(x-m)*(x-m);},0)/(n-1),s=Math.sqrt(s2);if(!s)return new CE(ET.DIV_BY_ZERO);
    var k=v.reduce(function(t,x){return t+Math.pow((x-m)/s,4);},0);return n*(n+1)/((n-1)*(n-2)*(n-3))*k-3*(n-1)*(n-1)/((n-2)*(n-3));}.bind(this));}
  trim(ast,st){return this.runFunction(ast.args,st,this.metadata('TRIMMEAN'),function(r,p){var v=nums(this,r).sort(function(a,b){return a-b;});if(p<0||p>=1)return new CE(ET.NUM);var k=Math.floor(v.length*p);k-=k%2;v=v.slice(k/2,v.length-k/2);return v.reduce(function(s,x){return s+x;},0)/v.length;}.bind(this));}
}
var R={argumentType:T.RANGE},N={argumentType:T.NUMBER},A={argumentType:T.ANY};
P.implementedFunctions={
  'MODE.SNGL':{method:'mode',parameters:[A],repeatLastArgs:1,expandRanges:false},
  'MODE':{method:'mode',parameters:[A],repeatLastArgs:1},
  'QUARTILE.INC':{method:'quart',parameters:[R,N]},'QUARTILE':{method:'quart',parameters:[R,N]},
  'PERCENTILE.INC':{method:'perc',parameters:[R,N]},'PERCENTILE':{method:'perc',parameters:[R,N]},
  'FORECAST.LINEAR':{method:'fore',parameters:[N,R,R]},'FORECAST':{method:'fore',parameters:[N,R,R]},
  'INTERCEPT':{method:'inter',parameters:[R,R]},
  'KURT':{method:'kurt',parameters:[A],repeatLastArgs:1},
  'TRIMMEAN':{method:'trim',parameters:[R,N]}
};
var es={'MODE.SNGL':'MODA.UNO','MODE':'MODA','QUARTILE.INC':'CUARTIL.INC','QUARTILE':'CUARTIL','PERCENTILE.INC':'PERCENTIL.INC','PERCENTILE':'PERCENTIL','FORECAST.LINEAR':'PRONOSTICO.LINEAL','FORECAST':'PRONOSTICO','INTERCEPT':'INTERSECCION.EJE','KURT':'CURTOSIS','TRIMMEAN':'MEDIA.ACOTADA'};
var en={};Object.keys(es).forEach(function(k){en[k]=k;});
var L=H.languages.esES;L.functions['SKEW.P']='COEFICIENTE.ASIMETRIA.P';L.functions['COVARIANCE.P']='COVARIANZA.P';
if(H.getRegisteredLanguagesCodes().indexOf('esES')<0)H.registerLanguage('esES',L);
H.registerFunctionPlugin(P,{esES:es,enGB:en});
})(window.HyperFormula);
