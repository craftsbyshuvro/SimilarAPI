DB_CON_STRING = 'D:\Study\Final Project\Applications\MyFirstPlugin\SQLiteDB\SimilarAPISample.db'

ALPHA = 0.3  # API Sequence Similarity Weight
BETA = 0.5  # Method Name Similarity Weight
GAMMA = 0.2  # Method Comment Similarity Weight

LIBRARY_COMMON_PREFIX = ["org.geotools.", "org.apache.bcel.", "org.atmosphere.", "org.springframework.xd.",
                         "org.jdom2.", "org.jdom.", "org.mockito.", "io.dropwizard.", "com.mysema.query.",
                         "org.flywaydb.", "com.thoughtworks.xstream.", "org.glassfish.tyrus.", "com.jme3.",
                         "org.springframework.data.jpa.", "com.vividsolutions.jts.", "org.apache.kafka.", "retrofit.",
                         "org.openxava.", "net.sf.launch4j.", "liquibase.", "org.apache.mina.", "prefuse.",
                         "org.htmlcleaner.", "org.junit.", "org.hamcrest.", "org.easymock.", "com.aliasi.",
                         "org.lwjgl.", "net.thucydides.", "org.aspectj.", "org.json.", "com.sun.j3d.", "org.activiti.",
                         "org.glassfish.grizzly.", "jxl.", "com.androidplot.", "org.jfree.chart.",
                         "org.springframework.ldap.", "org.zkoss", "jxl.", "ru.yandex.qatools.allure.", "org.jgrapht.",
                         "org.springframework.ws.", "com.fasterxml.jackson.", "com.hazelcast.", "org.eclipse.birt.",
                         "edu.stanford.nlp.", "org.apache.pig.", "org.jbehave.", "org.jsoup.", "com.xuggle.",
                         "org.apache.commons.io", "org.springframework.data.rest.", "org.jxls.", "org.achartengine.",
                         "org.glassfish.jersey.", "com.owlike.genson.", "javax.mail.", "org.infinispan.",
                         "org.apache.wss4j.", "net.sourceforge.jpcap.", "org.apache.solr.", "org.bonitasoft.engine.",
                         "javax.xml.ws.", "org.apache.solr.client.solrj.", "org.forgerock.opendj.",
                         "org.newdawn.slick.", "org.springframework.data.solr.", "com.googlecode.charts4j.",
                         "javassist.", "io.selendroid.", "org.apache.commons.mail.", "org.apache.olingo.",
                         "org.springframework.data.", "com.jogamp.", "org.apache.jena.", "org.springframework.session.",
                         "org.supercsv.", "org.jgroups.", "org.custommonkey.xmlunit.", "org.xmlunit.", "javax.ws.rs.",
                         "opennlp.", "org.appfuse.", "net.sf.fmj.", "org.apache.wink.", "org.apache.tika.",
                         "com.itextpdf.", "org.apache.poi.", "org.apache.commons.lang.", "org.powermock.api.",
                         "com.google.gson.", "mockit.", "org.odata4j.", "com.opencsv.", "org.apache.lucene.",
                         "org.thymeleaf.", "uk.co.caprica.vlcj.", "org.springframework.webflow.", "net.fortuna.ical4j.",
                         "io.appium.", "com.google.common.io.", "org.beanio.", "org.jmock.", "net.sf.jasperreports.",
                         "org.gephi.", "net.sf.cglib.", "com.jaunt.", "org.apache.tapestry5.", "com.vaadin.",
                         "org.jzy3d.", "org.dom4j.", "com.octo.android.robospice.", "org.jboss.resteasy.", "gate.",
                         "org.apache.log4j.", "cucumber.api.", "com.datastax.driver.", "org.hdiv.",
                         "org.springframework.data.hadoop.", "edu.uci.ics.jung.", "org.sitemesh.", "com.install4j.",
                         "org.apache.oozie.", "org.springframework.security.oauth2.", "javax.xml.", "org.coode.owlapi.",
                         "org.semanticweb.owlapi.", "com.clarkparsia.owlapi.", "de.uulm.ecs.ai.owlapi.",
                         "uk.ac.manchester.cs.owlapi.", "org.apache.pdfbox.", "com.netflix.astyanax.", "org.gridgain.",
                         "com.unboundid.ldap.sdk.", "org.testng.", "org.slf4j.", "com.google.common.base."]
